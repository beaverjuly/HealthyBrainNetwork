import pandas as pd
from .io import Paths

def validate_all(paths: Paths):
    paths.reports.mkdir(parents=True, exist_ok=True)

    rows = []
    for f in paths.interim.glob("*.csv"):
        real = pd.read_csv(f)
        syn = pd.read_csv(paths.synth / f.name)

        rows.append({
            "file": f.name,
            "real_rows": len(real),
            "syn_rows": len(syn),
            "real_cols": real.shape[1],
            "syn_cols": syn.shape[1],
        })

    report = pd.DataFrame(rows)
    out = paths.reports / "rowcol_check.csv"
    report.to_csv(out, index=False)
    print(f"[validate] wrote {out}")