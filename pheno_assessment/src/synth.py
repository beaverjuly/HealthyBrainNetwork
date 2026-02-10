import numpy as np
import pandas as pd
from pathlib import Path
from .io import Paths

def synthesize_table(df: pd.DataFrame, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    # baseline: sample rows with replacement (preserves marginals but not relationships well)
    idx = rng.integers(0, len(df), size=len(df))
    return df.iloc[idx].reset_index(drop=True)

def synthesize_all_tables(paths: Paths, seed: int = 0):
    paths.synth.mkdir(parents=True, exist_ok=True)
    for interim_file in paths.interim.glob("*.csv"):
        df = pd.read_csv(interim_file)
        syn = synthesize_table(df, seed=seed)
        out = paths.synth / interim_file.name
        syn.to_csv(out, index=False)
        print(f"[synth] wrote {out}")