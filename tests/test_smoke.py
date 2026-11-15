from pathlib import Path
import unittest
from code.engine import Engine, CurrencyError
from decimal import Decimal
from datetime import date

class SmokeTest(unittest.TestCase):
    def test_dataset_loads_and_images_resolve(self):
        engine=Engine(Path('dataset'))
        self.assertEqual(len(engine.requests),250)
        self.assertEqual(len(engine.extractions),16)
        self.assertTrue(all(item.amount is not None for item in engine.extractions.values()))

    def test_output_invariants_and_unknown_fx(self):
        engine=Engine(Path('dataset'))
        rows=engine.run()
        self.assertEqual(len(rows), 250)
        self.assertTrue(all(Decimal(row['amount_safe_to_pay']) >= 0 for row in rows))
        with self.assertRaises(CurrencyError):
            engine.convert(Decimal('1'), 'ZAR', 'INR', date(2019, 1, 1))
