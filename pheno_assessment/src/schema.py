from pathlib import Path
import pandas as pd

def get_column_map(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str, keep_default_na=False, nrows=1)
    raw = df.columns.tolist()
    std = [c.replace(",", "_") for c in raw]
    return pd.DataFrame({"raw": raw, "standardized": std})

def write_column_map(path: Path, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    get_column_map(path).to_csv(out_path, index=False)