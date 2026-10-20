# Pagoda Held-Out Benign Evaluation

Date: October 20, 2026

Training graphs: ADM-300 through ADM-304
Held-out benign graphs: ADM-370, 371, 372, 373, 375

Path threshold: 0.0001003259818015522
Graph threshold: approximately 0.1038

Results:
ADM-370: 0.450929, flagged
ADM-371: 0.468999, flagged
ADM-372: 0.469934, flagged
ADM-373: 0.462828, flagged
ADM-375: 0.443069, flagged

False positives: 5/5
Held-out false-positive rate: 100%

All five graphs were flagged at the graph level,
not the path level.

Limitations:
- Only five benign graphs used for training.
- Only five held-out benign graphs evaluated.
- Graph threshold was selected using benign and attack data.
- This result should not be presented as the published
  Pagoda false-positive rate.
