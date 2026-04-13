import pandas as pd
import os

# ── Read from previous step ──────────────────────────────────────────────────
transformed = pd.read_csv("data/03_transformed.csv")

# ── Select and order final columns ───────────────────────────────────────────
final = transformed[[
    "restaurant",
    "city",
    "currency",
    "revenue",
    "revenue_sek",
    "covers",
    "rev_per_cover",
    "rating",
    "revenue_tier"
]].copy()

# ── Publish ──────────────────────────────────────────────────────────────────
os.makedirs("output", exist_ok=True)
final.to_csv("output/restaurants_clean.csv", index=False)

print(f"✓ Published {len(final)} rows → output/restaurants_clean.csv")
print(final)
