import pandas as pd

# ── Read from previous step ──────────────────────────────────────────────────
raw = pd.read_csv("data/01_raw.csv")

# ── Clean ────────────────────────────────────────────────────────────────────

# Strip whitespace and normalize casing on text columns
cleaned = raw.copy()

cleaned[["restaurant", "city"]] = (
    cleaned[["restaurant", "city"]]
    .map(lambda x: x.strip().capitalize() if isinstance(x, str) else x)
)

# Convert revenue and covers to numeric — coerce bad values to NaN, then fill 0
cleaned[["revenue", "covers"]] = (
    cleaned[["revenue", "covers"]]
    .apply(pd.to_numeric, errors="coerce")
    .fillna(0)
)

# Convert rating to numeric and clip to valid range 0–5
cleaned["rating"] = (
    pd.to_numeric(cleaned["rating"], errors="coerce")
    .clip(upper=5.0)
)

# Remove duplicates — keep first occurrence
cleaned = cleaned.drop_duplicates(subset=["restaurant", "city"], keep="first")

# ── Write to intermediate file ───────────────────────────────────────────────
cleaned.to_csv("data/02_cleaned.csv", index=False)

print(f"✓ Cleaned {len(cleaned)} rows → data/02_cleaned.csv")
print(cleaned)
