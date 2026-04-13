import pandas as pd

# ── Read from previous step ──────────────────────────────────────────────────
cleaned = pd.read_csv("data/02_cleaned.csv")

# ── Transform ────────────────────────────────────────────────────────────────
EXCHANGE_RATES = {"SEK": 1.0, "DKK": 1.45, "NOK": 0.98}

transformed = cleaned.copy()

# Add exchange rate lookup
transformed["rate"] = transformed["currency"].map(EXCHANGE_RATES)

# Normalise revenue to SEK
transformed["revenue_sek"] = transformed["revenue"] * transformed["rate"]

# Revenue per cover — avoid division by zero (covers=0 already flagged in clean step)
transformed["rev_per_cover"] = (
    (transformed["revenue_sek"] / transformed["covers"].replace(0, float("nan")))
    .round(1)
)

# Segment into revenue tiers
transformed["revenue_tier"] = pd.cut(
    transformed["revenue_sek"],
    bins=[0, 50000, 100000, float("inf")],
    labels=["Low", "Medium", "High"]
)

# ── Write to intermediate file ───────────────────────────────────────────────
transformed.to_csv("data/03_transformed.csv", index=False)

print(f"✓ Transformed {len(transformed)} rows → data/03_transformed.csv")
print(transformed)
