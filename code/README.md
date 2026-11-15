# Buy or Wait? Submission Package

## Contents

This directory contains the complete Python source for the deterministic
financial decision engine:

- `engine.py` - reconstructs financial state, forecasts supported cashflows,
  checks 90-day safety, and selects a payment decision.
- `main.py` - generates `dataset/output.csv`.
- `validate.py` - validates the output schema, plans, deadlines, and safety.
- `evaluate.py` - evaluates the 25 public sample requests.
- `image_amounts.py` - performs the optional image-amount extraction audit.
- `__init__.py` - makes `code` runnable as a Python package.

## Requirements

- Python 3.11 or newer
- No required third-party packages
- Run commands from the project root, the directory containing `dataset/`

## Run the solution

From the project root:

```powershell
python -m code.main --dataset dataset
```

This reads the supplied dataset files and writes the completed
`dataset/output.csv`. It also writes the image extraction audit to
`evaluation/image_extraction_audit.json`.

## Validate the generated output

```powershell
python -m code.validate --dataset dataset --output dataset/output.csv
```

The command prints `VALID` when the output has the required columns, one row
per request, valid payment plans, supported spending changes, and safe
90-day balances.

## Evaluate the public samples

```powershell
python -m code.evaluate
```

This reports exact-field accuracy and affordability-status plus recommended
payment-method accuracy for the 25 labeled sample requests.

## Approach overview

The engine is deterministic and uses only the supplied project data. It:

1. Reconstructs each user's balance, minimum required balance, preferences,
   protected spending, and supported adjustable spending.
2. Resolves supplied financial events, messages, images, settlement states,
   and dated exchange rates without using live financial data.
3. Detects recurring cashflows only when the historical evidence supports a
   cadence, while handling supported event deduplication and payroll
   lifecycle/date evidence.
4. Simulates the request and projected cashflows across the 90-day safety
   horizon, ensuring the balance does not fall below the user's minimum.
5. Builds only payment plans supported by the request's payment options and
   user preferences.
6. Ranks safe plans using completion deadline, spending changes, payment
   cost, start date, and number of payments.

The submitted `dataset/output.csv` is the generated production prediction
file. Input dataset files are not modified by the source code.
