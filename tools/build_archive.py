"""Rebuild reading pages and catalog from local archive data."""
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parent
for script in ["build_researchers.py", "build_companies.py", "build_indexes.py"]:
    runpy.run_path(str(ROOT / script), run_name="__main__")
