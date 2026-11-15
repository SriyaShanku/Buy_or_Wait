from __future__ import annotations
import csv, re
from datetime import date
from decimal import Decimal
from pathlib import Path
from .engine import Engine, OUTPUT_COLUMNS, Payment, Change, dec, d

STATUSES={"affordable_now","affordable_with_plan","affordable_later","not_affordable"}; METHODS={"full_payment","partial_payment","installments","wait","not_recommended"}
PLAN=re.compile(r"^\d{4}-\d{2}-\d{2}:-?\d+(?:\.\d+)?(?:\|\d{4}-\d{2}-\d{2}:-?\d+(?:\.\d+)?)*$")
def parse_plan(text): return [] if text=="none" else [Payment(d(x.split(":",1)[0]), -dec(x.split(":",1)[1])) for x in text.split("|")]
def parse_changes(text):
    if text == 'none': return ()
    answer=[]
    for value in text.split('|'):
        parts=value.split(':')
        if parts[0]=='stop' and len(parts)==2: answer.append(Change(parts[1],'stop'))
        elif parts[0]=='reduce_to' and len(parts)==3: answer.append(Change(parts[1],'reduce',dec(parts[2])))
        else: raise ValueError(value)
    return tuple(answer)
def validate(dataset: Path, output: Path) -> list[str]:
    engine=Engine(dataset); errors=[]
    with output.open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f)); fields=f.readable() and f.seek(0) is None
    if not rows and len(engine.requests): errors.append("no output rows")
    with output.open(encoding="utf-8",newline="") as f: header=next(csv.reader(f))
    if header != OUTPUT_COLUMNS: errors.append("output header is not exact")
    expected={x['request_id']:x for x in engine.requests}; seen=set()
    for row in rows:
        rid=row.get('request_id',''); req=expected.get(rid)
        if not req: errors.append(f"unknown request {rid}"); continue
        if rid in seen: errors.append(f"duplicate request {rid}"); continue
        seen.add(rid); amount=dec(row['amount_safe_to_pay'])
        if amount is None or amount<0 or amount>(dec(req['requested_amount']) or Decimal(0)): errors.append(f"invalid safe amount {rid}")
        if row['affordability_status'] not in STATUSES or row['recommended_payment_method'] not in METHODS: errors.append(f"invalid enum {rid}")
        valid_pair={'affordable_now':{'full_payment'},'affordable_with_plan':{'full_payment','partial_payment','installments'},'affordable_later':{'wait'},'not_affordable':{'not_recommended'}}
        if row['recommended_payment_method'] not in valid_pair.get(row['affordability_status'],set()): errors.append(f"invalid status/method pair {rid}")
        if row['payment_plan']!='none' and not PLAN.match(row['payment_plan']): errors.append(f"bad plan syntax {rid}"); continue
        plan=parse_plan(row['payment_plan'])
        if plan and plan != sorted(plan,key=lambda x:x.when): errors.append(f"nonchronological plan {rid}")
        if plan and max(x.when for x in plan)>d(req['desired_completion_date']): errors.append(f"deadline miss {rid}")
        if row['earliest_date_for_full_payment']:
            try: d(row['earliest_date_for_full_payment'])
            except ValueError: errors.append(f"invalid earliest date {rid}")
        if row['affordability_status']=='affordable_now' and row['earliest_date_for_full_payment'] != req['request_date']: errors.append(f"affordable_now date {rid}")
        if row['recommended_payment_method']=='partial_payment':
            if len(plan)!=2 or row['affordability_status']!='affordable_with_plan' or sum((-x.amount for x in plan),Decimal(0)) != dec(req['requested_amount']): errors.append(f"invalid partial plan {rid}")
            if not (req['allows_partial_payment']=='true' and plan[0].when==d(req['request_date']) and plan[0].amount==-amount): errors.append(f"partial constraints {rid}")
        if row['recommended_payment_method'] in {'full_payment','wait'} and plan and sum((-x.amount for x in plan),Decimal(0)) != dec(req['requested_amount']): errors.append(f"wrong full total {rid}")
        if row['recommended_payment_method']=='installments':
            matches=[]
            for option in engine.options_by_request[rid]:
                if option['payment_method']=='installments' and [(x.when,-x.amount) for x in plan]==[(x.when,-x.amount) for x in engine._option_plan(req,option)]: matches.append(option)
            if not matches: errors.append(f"installment option mismatch {rid}")
        changes=row['spending_changes_needed']
        try: change_objects=parse_changes(changes)
        except ValueError: errors.append(f"bad changes {rid}"); change_objects=()
        if len(change_objects)>3 or len({x.event_id for x in change_objects}) != len(change_objects): errors.append(f"invalid changes {rid}")
        permitted={x.event_id for x in engine.available_changes(req)}
        if any(x.event_id not in permitted for x in change_objects): errors.append(f"unsupported changes {rid}")
        if plan and not engine.safe(req, plan, change_objects): errors.append(f"unsafe 90-day plan {rid}")
        if row['recommended_payment_method']=='not_recommended' and (plan or row['earliest_date_for_full_payment']): errors.append(f"not_recommended content {rid}")
    if seen != set(expected): errors.append(f"missing outputs: {len(set(expected)-seen)}")
    return errors
def main():
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--dataset',default='dataset');p.add_argument('--output',default='dataset/output.csv');a=p.parse_args()
    errors=validate(Path(a.dataset),Path(a.output)); print('VALID' if not errors else '\n'.join(errors)); raise SystemExit(bool(errors))
if __name__=='__main__':main()
