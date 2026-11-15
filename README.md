# Buy or Wait

Run from the project root with Python 3.11+:

```powershell
python -m code.main --dataset dataset
python -m code.validate --dataset dataset --output dataset/output.csv
python -m code.evaluate
```

The runner reads only supplied dataset inputs and overwrites only `dataset/output.csv`.
It uses `Decimal`, dated supplied FX rates, evidence-aware event reconstruction, a 90-day daily safety forecast, supplied payment schedules, and deterministic plan ranking. `code/image_amounts.py` isolates image extraction and writes `evaluation/image_extraction_audit.json`. Tesseract is optional; reviewed receipt totals are an explicit fallback, never a zero-default.
