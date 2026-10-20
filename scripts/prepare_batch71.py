import zipfile
import shutil
from pathlib import Path

archive = Path(
    "StreamSpot-Evasion-Graphs/train-test-provdetector-fga-pagoda.zip"
)

destination = Path("experiment/batch71/train")
destination.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(archive) as z:
    files = sorted(
        name for name in z.namelist()
        if name.startswith("tajka/trainGraphs/")
        and name.endswith(".csv")
    )

    print(f"Training graphs found: {len(files)}")

    if len(files) != 71:
        raise RuntimeError("Expected exactly 71 training graphs.")

    for index, source in enumerate(files, start=1):
        filename = Path(source).name

        with z.open(source) as src:
            with (destination / filename).open("wb") as dst:
                shutil.copyfileobj(src, dst)

        print(f"[{index}/71] Extracted {filename}")

print("\nAll 71 training graphs extracted successfully.")
