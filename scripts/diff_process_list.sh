#!/bin/bash
# Script to diff process list between core evidence and baseline evidence.
# File paths - Amend file paths accordingly to where the files are stored.

COREPROCESSLIST=/home/ubuntu/Stitcher/output/core/processlist.txt
BASELINEPROCESSLIST=/home/ubuntu/Stitcher/output/baseline/processlist.txt

diff $COREPROCESSLIST $BASELINEPROCESSLIST
