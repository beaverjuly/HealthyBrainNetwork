import pandas as pd
from pathlib import Path
from .io import Paths

def clean_table(raw_path: Path) -> pd.DataFrame:
    df = pd.read_csv(raw_path)
    # TODO: standardize missingness, types, rename keys
    return df

def clean_all_tables(paths: Paths):
    paths.interim.mkdir(parents=True, exist_ok=True)
    for raw_file in paths.raw.glob("*.csv"):
        df = clean_table(raw_file)
        out = paths.interim / raw_file.name
        df.to_csv(out, index=False)
        print(f"[clean] wrote {out}")