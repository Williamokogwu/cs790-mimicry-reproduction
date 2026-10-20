# Pagoda Full-Training Experiment

Date: October 20, 2026

## Configuration
- Benign training graphs: 71
- Original attack graphs: 5
- Mimicry-evasion graphs: 5
- Held-out benign graphs: Not yet evaluated
- Implementation: Original Pagoda source code

## Raw Output
fpr: 0
tpr: 5
evasion: 0

## Interpretation
- Training benign graphs flagged: 0/71
- Original attacks detected: 5/5 (100%)
- Mimicry-evasion graphs detected: 0/5 (0%)
- Mimicry-evasion graphs escaping detection: 5/5 (100%)

## Comparison with Five-Graph Training
- Five-graph training: 5/5 evasion graphs detected
- Seventy-one-graph training: 0/5 evasion graphs detected

## Limitations
- Only five original attack graphs evaluated.
- Only five mimicry-evasion graphs evaluated.
- The fpr output refers to training graphs, not held-out benign graphs.
- Held-out false-positive performance remains to be evaluated.
- The original implementation uses attack data when selecting its graph threshold.
