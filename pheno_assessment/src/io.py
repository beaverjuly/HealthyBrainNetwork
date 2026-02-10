from dataclasses import dataclass
from pathlib import Path

@dataclass
class Paths:
    root: Path
    raw: Path
    interim: Path
    synth: Path
    reports: Path

def get_paths(project_root: str) -> Paths:
    root = Path(project_root)
    return Paths(
        root=root,
        raw=root / "data" / "raw",
        interim=root / "data" / "interim",
        synth=root / "data" / "synth",
        reports=root / "data" / "reports",
    )