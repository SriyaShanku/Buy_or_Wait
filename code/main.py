from __future__ import annotations
import argparse, csv
from pathlib import Path
from .engine import Engine, OUTPUT_COLUMNS

def main() -> None:
    parser = argparse.ArgumentParser(description="Deterministic Buy or Wait runner")
    parser.add_argument("--dataset", default="dataset")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    dataset = Path(args.dataset); output = Path(args.output) if args.output else dataset / "output.csv"
    engine = Engine(dataset); rows = engine.run()
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS); writer.writeheader(); writer.writerows(rows)
    engine.write_audit(Path("evaluation") / "image_extraction_audit.json")
    print(f"wrote {len(rows)} rows to {output}")

if __name__ == "__main__": main()
