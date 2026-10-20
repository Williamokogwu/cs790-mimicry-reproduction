# Pagoda Held-Out Benign Evaluation — 71 Training Graphs

Date: October 20, 2026

## Configuration
- Benign training graphs: 71
- Held-out benign test graphs: 5
- Path threshold: 0.00010044666319354292
- Graph threshold: approximately 0.1237

## Results
ADM-370: score=0.450928, falsely flagged
ADM-371: score=0.468998, falsely flagged
ADM-372: score=0.469933, falsely flagged
ADM-373: score=0.446472, falsely flagged
ADM-375: score=0.443068, falsely flagged

False positives: 5/5
Held-out false-positive rate: 100%

All five benign graphs were flagged at the graph level.
None were flagged at the path level.

## Interpretation
Increasing benign training from 5 to 71 graphs did not
improve false-positive performance on these five test graphs.

## Limitations
- Only five held-out benign graphs evaluated.
- The graph threshold was calibrated using attack data.
- The evaluation protocol may differ from the original paper.
- These results do not establish the published Pagoda FPR.
