from pathlib import Path
import runpy

# ── Run all pipeline steps in sequence ───────────────────────────────────────
# This is the equivalent of sourcing your R scripts in order.
# You can also just run each .py file manually one at a time.

base = Path.cwd() /"publish_teams" / "W15" / "pipeline"

steps = [
    base / "01_load.py",
    base / "02_clean.py",
    base / "03_transform.py",
    base / "04_publish.py",
]

for step in steps:
    print(f"\n{'─' * 50}")
    print(f"  Running {step}")
    print(f"{'─' * 50}")
    runpy.run_path(step)

print("\n✓ Pipeline complete.")
