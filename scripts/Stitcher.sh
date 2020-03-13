#!/bin/bash
# Script to process core evidence and baseline evidence, and then correlate the processed evidence. Please execute this script with sudo.
# File paths - Amend file paths accordingly to where the files are stored.

PROCESSCORE=/home/ubuntu/Stitcher/scripts/process_core.py
PROCESSBASELINE=/home/ubuntu/Stitcher/scripts/process_baseline.py
CORRELATECORE=/home/ubuntu/Stitcher/scripts/correlate_core.py
CORRELATEBASELINE=/home/ubuntu/Stitcher/scripts/correlate_baseline.py

python3 $PROCESSCORE
python3 $PROCESSBASELINE
python3 $CORRELATECORE
python3 $CORRELATEBASELINE
