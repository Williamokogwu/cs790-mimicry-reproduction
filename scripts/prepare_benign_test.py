import zipfile
import shutil
from pathlib import Path

archive = Path("StreamSpot-Evasion-Graphs/train-test-provdetector-fga-pagoda.zip")
destination = Path("experiment/batch5/benign-test")
destination.mkdir(parents=True, exist_ok=True)

ids = [370, 371, 372, 373, 375]

with zipfile.ZipFile(archive) as z:
    for number in ids:
        filename = f"output_ADM-{number}.csv"
        source = f"tajka/testGraphs/{filename}"

        with z.open(source) as src:
            with (destination / filename).open("wb") as dst:
                shutil.copyfileobj(src, dst)

        print(f"Extracted benign test: {filename}")

print("Held-out benign graphs ready.")
