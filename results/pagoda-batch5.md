# Pagoda Five-Graph Experiment

Date: October 20, 2026

## Dataset
- Training: ADM-300 through ADM-304 (5 graphs)
- Original attacks: ADM-500 through ADM-504 (5 graphs)
- Mimicry evasion: ADM-600 through ADM-604 (5 graphs)

## Original Pagoda Output
fpr: 0, tpr: 5, evasion: 5

## Results
- Training graphs flagged: 0/5 (0%)
- Original attacks detected: 5/5 (100%)
- Evasion graphs detected: 5/5 (100%)

## Interpretation
All five original attacks and all five evasion graphs were
detected by Pagoda in this experiment.

## Limitations
- Small sample size.
- Benign evaluation reused training graphs.
- Attack/evasion pairing has not been independently verified.
- Original output represents counts, not rates.
- Results do not establish general evasion effectiveness.
