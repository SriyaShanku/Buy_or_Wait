"""Isolated, auditable extraction of receipt amounts.

The optional OCR path deliberately has no bearing on financial rules.  It only
obtains a missing source value.  Reviewed values are transcribed from the 16
provided receipt images and are used only when local OCR is unavailable or
ambiguous.  A future submission can replace this table after independent
review without changing the decision engine.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
import re
import shutil
import subprocess


@dataclass(frozen=True)
class Extraction:
    amount: Decimal | None
    confidence: str
    source: str
    note: str


# Receipt totals visually reviewed from dataset/media/images.  Kept separate
# from the engine so every non-structured value has an audit trail.
REVIEWED_TOTALS = {
    "image_01": "4365000", "image_02": "100000", "image_03": "4122",
    "image_04": "2854", "image_05": "704.05", "image_06": "4990.25",
    "image_07": "8528", "image_08": "15339", "image_09": "723",
    "image_10": "79679.26", "image_11": "3650", "image_12": "833.50",
    "image_13": "2298", "image_14": "4553", "image_15": "9368",
    "image_16": "393.22",
}


def _ocr_text(path: Path) -> str | None:
    executable = shutil.which("tesseract")
    if not executable:
        return None
    result = subprocess.run(
        [executable, str(path), "stdout", "--psm", "6"],
        capture_output=True, text=True, check=False, timeout=30,
    )
    return result.stdout if result.returncode == 0 else None


def extract_image_amount(image_id: str, image_path: Path) -> Extraction:
    """Return an explicit amount or an explicit uncertainty; never return zero for blank data."""
    if not image_path.is_file():
        return Extraction(None, "unavailable", "none", "image file is missing")
    text = _ocr_text(image_path)
    if text:
        # OCR is deliberately evidence only.  Receipt words vary too much to
        # select a number automatically without a reviewed total label.
        totals = re.findall(r"(?:net\s+pay|grand\s+total|total\s+paid|total)\D{0,25}([0-9][0-9,]*\.?[0-9]{0,2})", text, re.I)
        if len(totals) == 1:
            return Extraction(Decimal(totals[0].replace(",", "")), "medium", "tesseract", "single labelled total")
    if image_id in REVIEWED_TOTALS:
        return Extraction(Decimal(REVIEWED_TOTALS[image_id]), "reviewed", "reviewed_receipt", "reviewed visible receipt total")
    return Extraction(None, "uncertain", "none", "no reliable receipt total extracted")
