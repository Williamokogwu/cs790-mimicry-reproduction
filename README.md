# CS 790: Mimicry Attack Reproduction

## Project Overview

This project is a partial reproduction of:

Goyal et al., "Sometimes, You Aren't What You Do: Mimicry Attacks against Provenance Graph Host Intrusion Detection Systems," NDSS 2023.

We investigate whether mimicry-modified provenance graphs can evade Pagoda, a provenance-based host intrusion detection system.

## Team

Group 4 - Networking

- Chijioke
- David

Course: CS 790
Instructor: Professor Zhen Zeng

## Research Objective

Compare Pagoda's detection behavior on:

1. Benign provenance graphs
2. Original attack graphs
3. Mimicry-evasion graphs

We also examine whether increasing the number of benign training graphs changes detection outcomes.

## Original Implementation

Research repository:
https://bitbucket.org/sts-lab/mimicry-provenance-generator

The original implementation and datasets are maintained separately from this repository.

## Experimental Environment

- Windows 11
- Python 3.11.9
- PyTorch CPU build
- 16 GB RAM
- Original Pagoda implementation

Additional Python dependencies include pandas, NetworkX, and tqdm.

## Dataset

We used the StreamSpot-Evasion-Graphs archives supplied with the original research implementation.

Available graphs included:

- 71 benign training graphs
- 29 held-out benign graphs
- 100 original attack graphs
- 100 mimicry-evasion graphs

Our evaluated attack and evasion subsets each contained five graphs.

## Experiments and Results

| Metric | 5 Benign Training Graphs | 71 Benign Training Graphs |
|---|---|---|
| Original attacks detected | 5/5 | 5/5 |
| Evasion graphs detected | 5/5 | 0/5 |
| Evasion graphs escaping detection | 0/5 | 5/5 |
| Training benign graphs flagged | 0/5 | 0/71 |
| Held-out benign graphs flagged | 5/5 | 5/5 |

The training-benign counts are in-sample observations, not independent false-positive estimates.

In the 71-graph training experiment, Pagoda detected all five original attacks but detected none of the five mimicry-evasion graphs.

This provides limited-sample qualitative support for the paper's central finding that mimicry modifications can evade provenance-based intrusion detection.

However, all five held-out benign graphs were classified as attacks under our evaluation procedure.

## Limitations

- Only five attack graphs, five evasion graphs, and five held-out benign graphs were evaluated.
- The observed held-out false-positive rate was 100% on this small sample.
- The original Pagoda pipeline uses attack scores during threshold calibration, so detection on those same attack graphs is not an independent test.
- We have not fully verified that our held-out scoring procedure matches the original paper's complete evaluation protocol.
- Experiments were conducted on a CPU-only laptop, limiting evaluation scale.

Therefore, our work should be interpreted as a partial reproduction of mimicry-evasion behavior, not a full reproduction of the paper's detection performance.

## Repository Structure

- `scripts/` - Dataset preparation and held-out evaluation scripts
- `results/` - Recorded experimental outcomes
- `docs/` - Project documentation and report materials, when added

## Reproduction Notes

The scripts in this repository were developed and executed within the directory structure of the original `mimicry-provenance-generator` repository.

To reproduce the experiments:

1. Clone the original research repository.
2. Configure Python 3.11.9 and install its required dependencies.
3. Obtain the StreamSpot-Evasion-Graphs archives.
4. Place the preparation and evaluation scripts in the original repository's `experiment/` directory.
5. Prepare the five-graph and 71-graph datasets using the relevant preparation scripts.
6. Run the original `pagoda/main.py` pipeline with the benign training, attack, and evasion directories.
7. Run the held-out evaluation scripts against the corresponding saved model artifacts.

The held-out evaluation scripts load locally generated PyTorch artifacts. Only load artifacts from trusted sources.

The Markdown files in `results/` contain the recorded experimental outcomes.

## Conclusion

We successfully executed the original Pagoda implementation and observed mimicry-evasion behavior when training on all 71 available benign training graphs.

However, our held-out benign evaluation produced five false positives out of five graphs. Consequently, the detector's overall classification performance was not successfully reproduced.

## Deadline

October 22, 2026, at 11:59 PM.
