import unittest
from pathlib import Path
from datetime import timedelta
from code.engine import Engine, d, Payment

class DeduplicationRegressionTest(unittest.TestCase):
    def setUp(self):
        self.engine = Engine(Path('dataset'))

    def test_request_04_unrelated_expense_does_not_suppress_income(self):
        """request_04: an unrelated nearby expense (school fee on June 11) must NOT suppress recurring salary projection on June 14."""
        r4 = next(x for x in self.engine.samples if x['request_id'] == 'request_04')
        start = d(r4['request_date'])
        end = start + timedelta(days=90)
        flows = self.engine._future_cashflows(r4['user_id'], start, end, ())
        salary_flows = [f for f in flows if f.when.month == 6 and f.when.year == 2024 and f.amount > 0]
        self.assertTrue(len(salary_flows) > 0, "Recurring salary on 2024-06-14 should not be suppressed by nearby education expense on 2024-06-11.")

    def test_request_24_unrelated_event_does_not_suppress_recurring_expense(self):
        """request_24: an unrelated nearby event (insurance payment on Jan 11) must NOT suppress recurring expense projections."""
        r24 = next(x for x in self.engine.samples if x['request_id'] == 'request_24')
        start = d(r24['request_date'])
        end = start + timedelta(days=90)
        flows = self.engine._future_cashflows(r24['user_id'], start, end, ())
        jan_expenses = [f for f in flows if f.when.month == 1 and f.when.year == 2026 and f.amount < 0]
        self.assertTrue(len(jan_expenses) > 0, "Recurring expenses in Jan 2026 should not be suppressed by nearby insurance event.")

if __name__ == '__main__':
    unittest.main()
