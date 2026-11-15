from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from statistics import median
from typing import Iterable

from .image_amounts import Extraction, extract_image_amount

ZERO = Decimal("0")
CENT = Decimal("0.01")
OUTPUT_COLUMNS = ["request_id", "amount_safe_to_pay", "affordability_status", "recommended_payment_method", "payment_plan", "earliest_date_for_full_payment", "spending_changes_needed", "decision_explanation"]


def dec(value: str | Decimal | None) -> Decimal | None:
    if value in (None, ""):
        return None
    return Decimal(str(value).replace(",", ""))


def money(value: Decimal) -> str:
    value = value.quantize(CENT, rounding=ROUND_HALF_UP)
    return format(value.normalize(), "f") if value != value.to_integral() else str(int(value))


def d(value: str) -> date:
    return date.fromisoformat(value[:10])


def pipe(value: str) -> set[str]:
    return {x for x in value.split("|") if x}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


@dataclass(frozen=True)
class Event:
    event_id: str; user_id: str; event_type: str; description: str; category: str
    direction: str; amount: Decimal | None; currency: str; event_date: date
    settlement_date: date | None; status: str; linked_event_id: str; flexibility: str
    minimum_allowed_amount: Decimal | None


@dataclass(frozen=True)
class Payment:
    when: date; amount: Decimal; option_id: str = ""


@dataclass(frozen=True)
class Change:
    event_id: str; action: str; new_amount: Decimal | None = None

    def text(self) -> str:
        return f"stop:{self.event_id}" if self.action == "stop" else f"reduce_to:{self.event_id}:{money(self.new_amount or ZERO)}"


class CurrencyError(ValueError):
    pass


class Engine:
    def __init__(self, dataset: Path):
        self.dataset = dataset
        self.profiles = {x["user_id"]: x for x in read_csv(dataset / "financial_profiles.csv")}
        self.requests = read_csv(dataset / "requests.csv")
        self.samples = read_csv(dataset / "sample_requests.csv")
        self.raw_events = read_csv(dataset / "financial_events.csv")
        self.images = {x["related_event_id"]: x for x in read_csv(dataset / "images.csv")}
        self.messages = read_csv(dataset / "messages.csv")
        self.messages_by_event: dict[str, list[dict[str, str]]] = defaultdict(list)
        for message in self.messages:
            if message["related_event_id"]:
                self.messages_by_event[message["related_event_id"]].append(message)
        for values in self.messages_by_event.values(): values.sort(key=lambda x: x["sent_at"])
        self.options = read_csv(dataset / "request_payment_options.csv")
        self.rates = read_csv(dataset / "exchange_rates.csv")
        self.extractions: dict[str, Extraction] = {}
        self.flow_cache: dict[tuple, list[Payment]] = {}
        self.events = self._load_events()
        self.events_by_user: dict[str, list[Event]] = defaultdict(list)
        self.events_by_id = {e.event_id: e for e in self.events}
        for event in self.events: self.events_by_user[event.user_id].append(event)
        self.options_by_request: dict[str, list[dict[str, str]]] = defaultdict(list)
        for option in self.options: self.options_by_request[option["request_id"]].append(option)
        self.rate_index: dict[tuple[str, str], list[tuple[date, Decimal]]] = defaultdict(list)
        for row in self.rates: self.rate_index[(row["from_currency"], row["to_currency"])].append((d(row["rate_date"]), dec(row["rate"]) or ZERO))
        for values in self.rate_index.values(): values.sort()
        self._validate_inputs()

    def _load_events(self) -> list[Event]:
        result = []
        for row in self.raw_events:
            amount = dec(row["amount"])
            if amount is None:
                image = self.images.get(row["event_id"])
                if image:
                    extraction = extract_image_amount(image["image_id"], self.dataset / "media" / "images" / f"{image['image_id']}.png")
                    self.extractions[row["event_id"]] = extraction
                    amount = extraction.amount
            result.append(Event(row["event_id"], row["user_id"], row["event_type"], row["description"], row["category"], row["direction"], amount, row["currency"], d(row["event_date"]), d(row["settlement_date"]) if row["settlement_date"] else None, row["status"], row["linked_event_id"], row["flexibility"], dec(row["minimum_allowed_amount"])))
        return result

    def _validate_inputs(self) -> None:
        all_requests = {x["request_id"]: x for x in self.requests + self.samples}
        if len(all_requests) != 275 or len(self.profiles) != 275:
            raise ValueError("unexpected request/profile cardinality")
        for event in self.events:
            if event.user_id not in self.profiles: raise ValueError(f"event has unknown user: {event.event_id}")
            if event.linked_event_id and event.linked_event_id not in {e.event_id for e in self.events}: raise ValueError(f"invalid linked event: {event.event_id}")
        for image_event, row in self.images.items():
            if image_event not in {e.event_id for e in self.events} or row["request_id"] not in all_requests: raise ValueError(f"invalid image relation: {row['image_id']}")
        for option in self.options:
            if option["request_id"] not in all_requests: raise ValueError(f"invalid option relation: {option['payment_option_id']}")
        for msg in self.messages:
            if msg["user_id"] not in self.profiles: raise ValueError(f"invalid message user: {msg['message_id']}")
            if msg["request_id"] and msg["request_id"] not in all_requests: raise ValueError(f"invalid message request: {msg['message_id']}")
            if msg["related_event_id"] and msg["related_event_id"] not in {e.event_id for e in self.events}: raise ValueError(f"invalid message event: {msg['message_id']}")
        unresolved = [e.event_id for e in self.events if e.amount is None]
        if unresolved: raise ValueError("unresolved image amounts: " + ", ".join(unresolved))

    def convert(self, amount: Decimal, source: str, target: str, when: date) -> Decimal:
        if source == target: return amount
        choices = self.rate_index.get((source, target), [])
        inverse = self.rate_index.get((target, source), [])
        usable = [x for x in choices if x[0] <= when]
        if usable: return amount * usable[-1][1]
        usable_inverse = [x for x in inverse if x[0] <= when]
        if usable_inverse and usable_inverse[-1][1] != ZERO: return amount / usable_inverse[-1][1]
        raise CurrencyError(f"no supplied rate for {source}->{target} on or before {when}")

    def _message_state(self, event: Event, as_of: date) -> Event:
        relevant = [m for m in self.messages_by_event.get(event.event_id, []) if d(m["sent_at"]) <= as_of]
        current = event
        for msg in relevant:
            text = msg["message_text"].lower()
            if re.search(r"cancel(?:led|led)?|dibatal", text): current = replace(current, status="cancelled")
            elif re.search(r"settled|paid in full|sudah dibayar", text): current = replace(current, status="settled")
            elif re.search(r"amend|revised|updated amount|jumlah.*(?:menjadi|sebesar)", text):
                values = re.findall(r"(?:idr|inr|zar|usd|eur|₹|\$|€)\s*([0-9][0-9,.]*)", msg["message_text"], re.I)
                if values: current = replace(current, amount=dec(values[-1]))
        return current

    def _is_recurring_key(self, e: Event) -> tuple[str, str, str] | None:
        if e.event_type not in {"expense", "subscription", "income", "debt_payment"}: return None
        if e.category in {"windfall", "work_expense", "investment"}: return None
        return e.direction, e.category, re.sub(r"\d+", "", e.description.lower()).strip()

    def _is_terminal_marker(self, e: Event) -> bool:
        return bool(re.search(r"\b(?:final|last|terminal|ended)\b", e.description.lower()))

    def _is_lifecycle_replacement(self, old: Event, current_events: list[Event]) -> bool:
        if old.direction != "credit" or old.category != "salary":
            return False
        old_text = old.description.lower()
        if not re.search(r"\b(?:before|prior to|pre[- ]?)\b.*\b(?:leave|absence|break)\b", old_text):
            return False
        return any(
            e.settlement_date and old.settlement_date
            and e.settlement_date > old.settlement_date
            and e.direction == old.direction
            and e.category == old.category
            and re.search(r"\b(?:after|upon)\b.*\b(?:return|returning|leave|absence)\b|\b(?:resumed|reinstated)\b", e.description.lower())
            for e in current_events
        )

    def _payroll_date_override(self, user_id: str, as_of: date) -> date | None:
        pattern = re.compile(
            r"\b(?:payroll|salary|pay)\b.*?"
            r"\b(?:confirmed|revised|revised date|replacement|replaces|expected|credit date|resumes?)\b.*?"
            r"\b(?:on|date is|date of)?\s*(\d{4}-\d{2}-\d{2})\b",
            re.I,
        )
        dates: list[date] = []
        for msg in self.messages:
            if msg["user_id"] != user_id or d(msg["sent_at"]) > as_of:
                continue
            match = pattern.search(msg["message_text"])
            if match:
                dates.append(d(match.group(1)))
        return max(dates) if dates else None

    def _future_cashflows(self, user_id: str, start: date, end: date, changes: tuple[Change, ...]) -> list[Payment]:
        cache_key = (user_id, start, end, tuple((c.event_id, c.action, c.new_amount) for c in changes))
        if cache_key in self.flow_cache:
            return self.flow_cache[cache_key]
        home = self.profiles[user_id]["home_currency"]
        changed = {c.event_id: c for c in changes}
        flows: list[Payment] = []
        flow_meta: list[tuple[date, str, str, tuple[str, str, str] | None]] = []
        explicit_dates: set[tuple[str, date]] = set()
        # Existing future events.  Pending credits, failed/cancelled, and non-cash valuations never enter cash flow.
        for original in self.events_by_user[user_id]:
            e = self._message_state(original, start)
            if not e.settlement_date or not (start <= e.settlement_date <= end): continue
            if e.status in {"failed", "cancelled", "unrealized"} or e.direction == "non_cash" or e.amount is None: continue
            if e.status == "pending" and e.direction == "credit": continue
            # A future settled salary is confirmed; other future settled entries are also explicit records.
            value = self.convert(e.amount, e.currency, home, e.settlement_date)
            sign = Decimal("1") if e.direction == "credit" else Decimal("-1")
            flows.append(Payment(e.settlement_date, sign * value)); explicit_dates.add((e.event_id, e.settlement_date))
            flow_meta.append((e.settlement_date, e.direction, e.category, self._is_recurring_key(e)))
        # Forecast only well-supported recurring series (at least two historical observations, monthly cadence).
        groups: dict[tuple[str, str, str], list[Event]] = defaultdict(list)
        for e in self.events_by_user[user_id]:
            state = self._message_state(e, start)
            if state.status in {"failed", "cancelled", "unrealized"} or not state.amount or not state.settlement_date: continue
            key = self._is_recurring_key(state)
            if key and state.settlement_date < start: groups[key].append(state)
        for key, rows in groups.items():
            rows.sort(key=lambda x: x.settlement_date or date.min)
            if len(rows) < 2: continue
            gaps = [(rows[i].settlement_date - rows[i-1].settlement_date).days for i in range(1, len(rows))]
            cadence = int(median(gaps[-4:]))
            if not 25 <= cadence <= 35: continue
            last = rows[-1]; amounts = [self.convert(x.amount or ZERO, x.currency, home, x.settlement_date or start) for x in rows[-3:]]
            value = Decimal(str(median(amounts)))
            terminal = [
                e for e in self.events_by_user[user_id]
                if e.settlement_date and e.settlement_date >= (last.settlement_date or date.min)
                and e.direction == key[0] and e.category == key[1]
                and self._is_terminal_marker(e)
                and (e.settlement_date - (last.settlement_date or date.min)).days <= cadence * 2
            ]
            if terminal:
                continue
            if any(self._is_lifecycle_replacement(row, self.events_by_user[user_id]) for row in rows):
                continue
            action = changed.get(last.event_id)
            if action:
                if action.action == "stop": value = ZERO
                elif action.new_amount is not None: value = self.convert(action.new_amount, last.currency, home, start)
            next_date = (last.settlement_date or start) + timedelta(days=cadence)
            if key[0] == "credit" and key[1] == "salary":
                override = self._payroll_date_override(user_id, start)
                if override and last.settlement_date < override <= end:
                    next_date = override
            while next_date <= end:
                # Avoid double counting explicit future event from the same recurrence anchor/category date.
                existing = any(abs((dt - next_date).days) <= 3 and (k == key or (d_dir == key[0] and cat == key[1])) for dt, d_dir, cat, k in flow_meta)
                if not existing and value:
                    sign = Decimal("1") if last.direction == "credit" else Decimal("-1")
                    flows.append(Payment(next_date, sign * value))
                    flow_meta.append((next_date, last.direction, last.category, key))
                next_date += timedelta(days=cadence)
        self.flow_cache[cache_key] = flows
        return flows

    def safe(self, request: dict[str, str], payments: Iterable[Payment], changes: tuple[Change, ...] = ()) -> bool:
        profile = self.profiles[request["user_id"]]; start = d(request["request_date"]); end = start + timedelta(days=90)
        balance = dec(profile["current_available_balance"]) or ZERO; minimum = dec(profile["minimum_balance_to_keep"]) or ZERO
        entries = self._future_cashflows(request["user_id"], start, end, changes) + list(payments)
        daily: dict[date, Decimal] = defaultdict(lambda: ZERO)
        for item in entries:
            if start <= item.when <= end: daily[item.when] += item.amount
        for day in (start + timedelta(days=i) for i in range(91)):
            balance += daily[day]
            if balance < minimum - CENT: return False
        return True

    def safe_amount_today(self, request: dict[str, str]) -> Decimal:
        amount = dec(request["requested_amount"]) or ZERO; today = d(request["request_date"])
        lo, hi = ZERO, amount
        for _ in range(48):
            mid = (lo + hi) / 2
            if self.safe(request, [Payment(today, -mid)]): lo = mid
            else: hi = mid
        return lo.quantize(CENT, rounding=ROUND_HALF_UP)

    def earliest_full(self, request: dict[str, str]) -> date | None:
        amount = dec(request["requested_amount"]) or ZERO; start = d(request["request_date"])
        for offset in range(91):
            when = start + timedelta(days=offset)
            if self.safe(request, [Payment(when, -amount)]): return when
        return None

    def available_changes(self, request: dict[str, str]) -> list[Change]:
        profile = self.profiles[request["user_id"]]; protected = pipe(profile["expense_categories_to_protect"]); reduce = pipe(profile["expense_categories_user_is_willing_to_reduce"]); stop = pipe(profile["expense_categories_user_is_willing_to_stop"])
        choices: list[tuple[Decimal, Change]] = []
        for e in self.events_by_user[request["user_id"]]:
            if e.category in protected or not e.amount or e.direction != "debit" or e.status in {"failed", "cancelled"}: continue
            if not self._is_recurring_key(e): continue
            if e.category in stop and e.flexibility in {"stoppable", "reducible_or_stoppable"}: choices.append((e.amount, Change(e.event_id, "stop")))
            elif e.category in reduce and e.flexibility in {"reducible", "reducible_or_stoppable"}:
                new = e.minimum_allowed_amount if e.minimum_allowed_amount is not None else e.amount / 2
                if new < e.amount: choices.append((e.amount - new, Change(e.event_id, "reduce", new)))
        return [x[1] for x in sorted(choices, key=lambda x: (-x[0], x[1].event_id))]

    def _option_plan(self, request: dict[str, str], option: dict[str, str]) -> list[Payment]:
        count = int(option["number_of_payments"]); first = d(option["first_payment_date"]); amount = dec(option["payment_amount"]) or ZERO
        total = dec(option["total_payable_amount"]) or amount * count; frequency = int(option["payment_frequency_days"] or 0)
        result = []
        for i in range(count):
            value = amount if i < count - 1 else total - amount * (count - 1)
            result.append(Payment(first + timedelta(days=frequency * i), -value, option["payment_option_id"]))
        return result

    def _format_plan(self, payments: list[Payment]) -> str:
        return "|".join(f"{x.when.isoformat()}:{money(-x.amount if x.amount < ZERO else x.amount)}" for x in sorted(payments, key=lambda x: x.when))

    def decide(self, request: dict[str, str]) -> dict[str, str]:
        requested = dec(request["requested_amount"]) or ZERO; start = d(request["request_date"]); deadline = d(request["desired_completion_date"])
        profile = self.profiles[request["user_id"]]; accepts = pipe(profile["payment_methods_user_will_consider"]); safe_now = self.safe_amount_today(request); earliest = self.earliest_full(request)
        candidates: list[tuple[tuple, str, list[Payment], tuple[Change, ...]]] = []
        def add(method: str, plan: list[Payment], changes: tuple[Change, ...] = (), option_id: str = ""):
            if not self.safe(request, plan, changes): return
            completed = max(x.when for x in plan) <= deadline
            total = -sum((x.amount for x in plan), ZERO)
            key = (0 if completed else 1, 0 if not changes else 1, total, min(x.when for x in plan), len(plan), option_id)
            candidates.append((key, method, plan, changes))
        if safe_now >= requested - CENT and "full_payment" in accepts: add("full_payment", [Payment(start, -requested)])
        if request["allows_partial_payment"].lower() == "true" and "partial_payment" in accepts and ZERO < safe_now < requested and earliest and earliest <= deadline:
            add("partial_payment", [Payment(start, -safe_now), Payment(earliest, -(requested-safe_now))])
        max_months = int(profile["max_installment_months"] or 0)
        for option in self.options_by_request[request["request_id"]]:
            if option["payment_method"] != "installments" or "installments" not in accepts: continue
            if max_months and int(option["number_of_payments"]) > max_months: continue
            add("installments", self._option_plan(request, option), (), option["payment_option_id"])
        # Spending changes are a last eligible way to create a safe plan; greedily test prefixes up to three.
        actions = self.available_changes(request)
        for n in range(1, min(3, len(actions)) + 1):
            changes = tuple(actions[:n])
            if "full_payment" in accepts: add("full_payment", [Payment(start, -requested)], changes)
            for option in self.options_by_request[request["request_id"]]:
                if option["payment_method"] == "installments" and "installments" in accepts and (not max_months or int(option["number_of_payments"]) <= max_months): add("installments", self._option_plan(request, option), changes, option["payment_option_id"])
        if candidates:
            _, method, plan, changes = min(candidates, key=lambda x: x[0])
            status = "affordable_now" if method == "full_payment" and not changes and plan[0].when == start else "affordable_with_plan"
            earliest_text = start.isoformat() if status == "affordable_now" else (earliest.isoformat() if earliest else "")
            reason = f"{method.replace('_', ' ')} keeps the projected balance above the {profile['home_currency']} {money(dec(profile['minimum_balance_to_keep']) or ZERO)} minimum over 90 days."
            return {"request_id": request["request_id"], "amount_safe_to_pay": money(min(safe_now, requested)), "affordability_status": status, "recommended_payment_method": method, "payment_plan": self._format_plan(plan), "earliest_date_for_full_payment": earliest_text, "spending_changes_needed": "|".join(c.text() for c in changes) if changes else "none", "decision_explanation": reason}
        if earliest and earliest <= deadline and "full_payment" in accepts:
            plan = [Payment(earliest, -requested)]
            if self.safe(request, plan):
                return {"request_id": request["request_id"], "amount_safe_to_pay": money(min(safe_now, requested)), "affordability_status": "affordable_later", "recommended_payment_method": "wait", "payment_plan": self._format_plan(plan), "earliest_date_for_full_payment": earliest.isoformat(), "spending_changes_needed": "none", "decision_explanation": f"Waiting until {earliest.isoformat()} protects the {profile['home_currency']} minimum balance."}
        return {"request_id": request["request_id"], "amount_safe_to_pay": money(min(safe_now, requested)), "affordability_status": "not_affordable", "recommended_payment_method": "not_recommended", "payment_plan": "none", "earliest_date_for_full_payment": "", "spending_changes_needed": "none", "decision_explanation": "No eligible plan maintains the required minimum balance through the 90-day forecast."}

    def run(self) -> list[dict[str, str]]:
        return [self.decide(request) for request in self.requests]

    def write_audit(self, path: Path) -> None:
        path.write_text(json.dumps({k: {"amount": money(v.amount) if v.amount is not None else None, "confidence": v.confidence, "source": v.source, "note": v.note} for k, v in self.extractions.items()}, indent=2), encoding="utf-8")

    def source_hashes(self) -> dict[str, str]:
        return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in self.dataset.glob("*.csv") if p.name != "output.csv"}
