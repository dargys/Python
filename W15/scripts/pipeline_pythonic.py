import pandas as pd
import os

# ── Constants ────────────────────────────────────────────────────────────────
EXCHANGE_RATES = {"SEK": 1.0, "DKK": 1.45, "NOK": 0.98}

# ── Pipeline functions ───────────────────────────────────────────────────────
def load(path: str) -> pd.DataFrame:
    '''
    1. load data when given a path from external source.
    '''
    df = pd.read_csv(path)
    print(f"✓ Loaded {len(df)} rows from {path}")
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    '''
    2. clean data for existing columns to ensure correct data type, missing values are handled, validated duplications are removed.
    '''
    return (
        df.copy()
        .assign(
            restaurant = lambda x: x["restaurant"].str.strip().str.capitalize(),
            city       = lambda x: x["city"].str.strip().str.capitalize(),
            revenue    = lambda x: pd.to_numeric(x["revenue"], errors="coerce").fillna(0),
            covers     = lambda x: pd.to_numeric(x["covers"],  errors="coerce").fillna(0),
            rating     = lambda x: pd.to_numeric(x["rating"],  errors="coerce").clip(upper=5.0),
        )
        .drop_duplicates(subset=["restaurant", "city"], keep="first")
    )


def transform(df: pd.DataFrame) -> pd.DataFrame:
    '''
    3. transform data to add calculated columns for further analysis.
    '''
    return (
        df.assign(
            rate          = lambda x: x["currency"].map(EXCHANGE_RATES),
            revenue_sek   = lambda x: x["revenue"] * x["rate"],
            rev_per_cover = lambda x: (x["revenue_sek"] / x["covers"].replace(0, float("nan"))).round(1),
            revenue_tier  = lambda x: pd.cut(
                                x["revenue_sek"],
                                bins=[0, 50000, 100000, float("inf")],
                                labels=["Low", "Medium", "High"]
                            ),
        )
    )


def publish(df: pd.DataFrame, path: str) -> None:
    '''
    4. publish: write to csv at given path to store cleaned and transformed data.
    '''
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"✓ Published {len(df)} rows → {path}")

