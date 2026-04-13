import pandas as pd
import os

# ── Raw data ────────────────────────────────────────────────────────────────
raw_data = [
    {"restaurant": "  pasta palace   ",  "city": "Stockholm",  "revenue": "182000",    "currency": "SEK", "covers": "210", "rating": "4.5"},
    {"restaurant": "Burger Barn  ",      "city": "Stockholm",  "revenue": "95000",     "currency": "SEK", "covers": "180", "rating": "3.8"},
    {"restaurant": "SUSHI SPOT",         "city": "Copenhagen", "revenue": "28000",     "currency": "DKK", "covers": "95",  "rating": "4.9"},
    {"restaurant": "taco town",          "city": " Oslo ",     "revenue": "61000",     "currency": "NOK", "covers": "140", "rating": None},
    {"restaurant": "Pasta Palace",       "city": "Stockholm",  "revenue": "182000",    "currency": "SEK", "covers": "210", "rating": "4.5"},
    {"restaurant": "Green Garden",       "city": "Oslo",       "revenue": "see notes", "currency": "NOK", "covers": "88",  "rating": "4.1  "},
    {"restaurant": "Burger Barn",        "city": "Copenhagen", "revenue": "31500",     "currency": "DKK", "covers": "210", "rating": "6.0"},
    {"restaurant": "  Ramen House ",     "city": "Stockholm",  "revenue": "74000",     "currency": "SEK", "covers": None,  "rating": "4.2"},
]

# ── Load into DataFrame and write to intermediate file ───────────────────────
raw = pd.DataFrame(raw_data)

os.makedirs("data", exist_ok=True)
raw.to_csv("data/01_raw.csv", index=False)

print(f"✓ Loaded {len(raw)} rows → data/01_raw.csv")
print(raw)
