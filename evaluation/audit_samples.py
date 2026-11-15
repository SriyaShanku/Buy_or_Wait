"""Write a compact, reproducible before/after audit of labeled samples."""
from collections import defaultdict
from datetime import timedelta
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from code.engine import Engine

CAUSE = {
 "request_01":"other (explanation only)", "request_02":"90-day forecast / earliest-full-payment calculation",
 "request_03":"90-day forecast / earliest-full-payment calculation", "request_04":"recurrence handling / 90-day forecast",
 "request_05":"recurrence handling / 90-day forecast", "request_06":"recurrence handling / spending-change logic",
 "request_07":"90-day forecast / earliest-full-payment calculation", "request_08":"90-day forecast / earliest-full-payment calculation",
 "request_09":"other (explanation only)", "request_10":"90-day forecast", "request_11":"recurrence handling / spending-change logic",
 "request_12":"other (explanation only)", "request_13":"90-day forecast / earliest-full-payment calculation",
 "request_14":"90-day forecast", "request_15":"90-day forecast", "request_16":"image amount interpretation / event status-lifecycle handling",
 "request_17":"90-day forecast / earliest-full-payment calculation", "request_18":"90-day forecast / earliest-full-payment calculation",
 "request_19":"payment-option selection / earliest-full-payment calculation", "request_20":"90-day forecast",
 "request_21":"recurrence handling / spending-change logic", "request_22":"90-day forecast / earliest-full-payment calculation",
 "request_23":"90-day forecast / earliest-full-payment calculation", "request_24":"90-day forecast", "request_25":"90-day forecast",
}
FIELDS=("amount_safe_to_pay","affordability_status","recommended_payment_method","payment_plan","earliest_date_for_full_payment","spending_changes_needed","decision_explanation")
def compact(events):
    return "; ".join(f"{x.event_id} {x.category}/{x.direction} {x.amount} {x.status} {x.settlement_date}" for x in events)
def main():
    e=Engine(Path("dataset")); lines=["# Sample mismatch audit", "", "Generated deterministically from the current engine and supplied labels. Event lists are limited to a 120-day evidence window.", ""]
    for r in e.samples:
        got=e.decide(r); differences=[f for f in FIELDS if got[f]!=r[f]]
        if not differences: continue
        when=__import__('datetime').date.fromisoformat(r['request_date']); p=e.profiles[r['user_id']]
        events=[x for x in e.events_by_user[r['user_id']] if x.settlement_date and abs((x.settlement_date-when).days)<=120]
        income=[x for x in events if x.direction=='credit'][-4:]; expenses=[x for x in events if x.direction=='debit'][-8:]
        grouped=defaultdict(list)
        for x in events:
            key=e._is_recurring_key(x)
            if key: grouped[x.category].append(x)
        recurring=[f"{category}: {','.join(x.event_id for x in rows[-3:])}" for category,rows in sorted(grouped.items()) if len(rows)>=2]
        future=[x for x in e.events_by_user[r['user_id']] if x.settlement_date and when<=x.settlement_date<=when+timedelta(days=90) and x.status in {'pending','scheduled'}]
        messages=[m for m in e.messages if m['user_id']==r['user_id'] and (m['request_id']==r['request_id'] or m['related_event_id'])]
        image=e.images.get(next((x.event_id for x in e.events_by_user[r['user_id']] if x.amount is not None and x.event_id in e.images),""))
        option_text='; '.join("{} {} {}x{} from {} total {}".format(o['payment_option_id'],o['payment_method'],o['payment_amount'],o['number_of_payments'],o['first_payment_date'],o['total_payable_amount']) for o in e.options_by_request[r['request_id']])
        lines += [f"## {r['request_id']} — {CAUSE.get(r['request_id'],'other')}",
          f"- First difference: `{differences[0]}`; all: {', '.join(differences)}.",
          f"- Expected: `{ ' | '.join(r[x] for x in FIELDS[:-1]) }`.", f"- Current: `{ ' | '.join(got[x] for x in FIELDS[:-1]) }`.",
          f"- Profile: start `{p['current_available_balance']}` {p['home_currency']}; minimum `{p['minimum_balance_to_keep']}`; methods `{p['payment_methods_user_will_consider']}`; deadline `{r['desired_completion_date']}`.",
          f"- Income evidence: {compact(income) or 'none'}.", f"- Expense evidence: {compact(expenses) or 'none'}.",
          f"- Recurrence candidates: {'; '.join(recurring) or 'none'}.", f"- Pending/scheduled: {compact(future) or 'none'}.",
          f"- Messages: {'; '.join(m['message_text'][:140] for m in messages) or 'none'}.",
          f"- Image evidence: {image['image_id'] + ' -> ' + str(e.extractions.get(image['related_event_id'])) if image else 'none'}.",
          f"- Options: {option_text}.", ""]
    Path("evaluation/sample_audit.md").write_text("\n".join(lines),encoding="utf-8")
if __name__=='__main__': main()
