# Pagoda Pilot Experiment

Date: October 17, 2026

## Environment
- Windows 11
- Python 3.11.9
- CPU execution
- Original Pagoda implementation

## Input Graphs
- Training: output_ADM-300.csv
- Attack: output_ADM-500.csv
- Evasion: output_ADM-600.csv

## Original Program Output
fpr: 0, tpr: 1, evasion: 1

## Interpretation
- Training graphs flagged: 0 of 1
- Original attack graphs detected: 1 of 1
- Evasion graphs detected: 1 of 1

The evasion graph was still detected in this pilot.

## Limitations
- Only one graph per category was evaluated.
- The original implementation uses training graphs for benign evaluation.
- The attack and evasion files have not been confirmed as a matched pair.
- The output labels represent detection counts, not normalized rates.
- Results are insufficient for general conclusions about evasion effectiveness.
