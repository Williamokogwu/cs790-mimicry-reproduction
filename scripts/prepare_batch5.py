import zipfile
from pathlib import Path

base = Path("StreamSpot-Evasion-Graphs")
output = Path("experiment/batch5")

jobs = [
    (
        base / "train-test-provdetector-fga-pagoda.zip",
        "tajka/trainGraphs/",
        "train",
        range(300, 305),
    ),
    (
        base / "provDetector-fga-pagoda-attack-evasion-graphs.zip",
        "attackGraphs/",
        "attack",
        range(500, 505),
    ),
    (
        base / "provDetector-fga-pagoda-attack-evasion-graphs.zip",
        "evasion/",
        "evasion",
        range(600, 605),
    ),
]

for archive, prefix, category, numbers in jobs:
    destination = output / category
    destination.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(archive) as z:
        for number in numbers:
            filename = f"output_ADM-{number}.csv"
            source = prefix + filename

            with z.open(source) as src:
                with (destination / filename).open("wb") as dst:
                    import shutil
                    shutil.copyfileobj(src, dst)

            print(f"Extracted {category}: {filename}")

print("\nBatch preparation complete.")
