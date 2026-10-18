# CS 790: Mimicry Attack Reproduction

## Project Overview

This project is a partial reproduction of the research paper:

"Sometimes, You Aren't What You Do: Mimicry Attacks against
Provenance Graph Host Intrusion Detection Systems"
(Goyal et al., NDSS 2023).

Our focus is on Pagoda, a provenance-based host intrusion
detection system evaluated in the original paper.

## Research Objective

Investigate whether mimicry-modified attack graphs reduce
Pagoda's ability to detect malicious activity compared
with unmodified attack graphs.

## Team

Group 4 - Networking
- Chijioke
- David

Course: CS 790
Instructor: Professor Zhen Zeng

## Project Status

Completed:
- Selected the research paper and Pagoda reproduction scope.
- Cloned the original researchers' repository.
- Configured Python 3.11.9 and verified dependencies.
- Identified training, benign, attack, and evasion datasets.
- Extracted four sample provenance graphs.
- Tested basic graph construction and path enumeration.

Pending:
- Run the complete Pagoda detection pipeline.
- Collect detection metrics.
- Compare results with the paper.
- Prepare the final two-page report.

## Original Research Code

https://bitbucket.org/sts-lab/mimicry-provenance-generator

The original research datasets and implementation are maintained
separately from this repository.

## Deadline

October 22, 2026, at 11:59 PM.
