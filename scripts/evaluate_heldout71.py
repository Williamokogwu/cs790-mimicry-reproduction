import os
import sys
import glob
from pathlib import Path

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pagoda"))

import pathsWrapper
import thresholdWrapper
import calcStatsWrapper

MODEL_DIR = ROOT / "experiment" / "pagoda-batch71"
TEST_DIR = ROOT / "experiment" / "batch5" / "benign-test"
OUTPUT_DIR = ROOT / "experiment" / "pagoda-heldout71"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load only caches generated locally by our own Pagoda run.
freqDB = torch.load(
    MODEL_DIR / "freqDB.pth",
    map_location="cpu",
    weights_only=False
)

results = torch.load(
    MODEL_DIR / "results.pth",
    map_location="cpu",
    weights_only=False
)

pathThreshold, graphThreshold, _, _, _ = results

print("Path threshold:", pathThreshold)
print("Graph threshold:", graphThreshold)

test_files = sorted(glob.glob(str(TEST_DIR / "*.csv")))

print("Held-out benign graphs:", len(test_files))

if len(test_files) != 5:
    raise RuntimeError("Expected exactly five held-out benign graphs.")

# Avoid accidentally loading cached scores from another experiment.
os.chdir(OUTPUT_DIR)

# Build graph paths using the previously trained frequency database.
test_paths, test_freq_db = pathsWrapper.generate(test_files, freqDB)

# Compute scores for previously unseen benign graphs.
graph_scores, all_path_scores = thresholdWrapper.getScoreWrapper(
    test_paths,
    test_freq_db,
    "heldout"
)

# Stage 1: path-level anomaly detection.
remaining_scores, path_caught = thresholdWrapper.prune(
    all_path_scores,
    pathThreshold,
    graph_scores
)

# Stage 2: graph-level anomaly detection for graphs not already flagged.
path_flags = [
    any(score >= pathThreshold for score in scores)
    for scores in all_path_scores
]

graph_flags = [
    (not path_flags[i]) and (score >= graphThreshold)
    for i, score in enumerate(graph_scores)
]

flags = [
    path_flags[i] or graph_flags[i]
    for i in range(len(test_files))
]

false_positives = sum(flags)
false_positive_rate = false_positives / len(test_files)

print("\nHELD-OUT BENIGN RESULTS")
print("-----------------------")

for filename, score, path_flag, graph_flag, flagged in zip(
    test_files, graph_scores, path_flags, graph_flags, flags
):
    print(
        f"{Path(filename).name}: "
        f"score={score:.6f}, "
        f"path_flag={path_flag}, "
        f"graph_flag={graph_flag}, "
        f"detected_as_attack={flagged}"
    )

print(f"\nFalse positives: {false_positives}/{len(test_files)}")
print(f"Held-out false-positive rate: {false_positive_rate:.2%}")
