from __future__ import annotations
from pathlib import Path
from .engine import Engine
def main():
    e=Engine(Path('dataset')); sample=[e.decide(x) for x in e.samples]
    fields=('amount_safe_to_pay','affordability_status','recommended_payment_method','payment_plan','earliest_date_for_full_payment','spending_changes_needed')
    exact=sum(all(g[k]==x[k] for k in fields) for g,x in zip(sample,e.samples))
    status_method=sum((g['affordability_status'],g['recommended_payment_method'])==(x['affordability_status'],x['recommended_payment_method']) for g,x in zip(sample,e.samples))
    print(f'sample exact rows: {exact}/{len(sample)}; status/method: {status_method}/{len(sample)}')
    print(f'image extractions: {len(e.extractions)}; unresolved: {sum(x.amount is None for x in e.extractions.values())}')
if __name__=='__main__':main()
