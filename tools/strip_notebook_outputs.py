import json
import sys
from pathlib import Path


def strip(path: Path) -> None:
    nb = json.loads(path.read_text(encoding="utf-8"))
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Stripped {path.name} ({len(nb['cells'])} cells, {path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    strip(Path(sys.argv[1]))
