#!/bin/bash
# Script to compare top TCP port with list of files that had strings executed earlier.
# File paths - Amend file paths accordingly to where the files are stored.

PORTFILE=/home/ubuntu/Stitcher/output/core/topTCPport.txt
STRINGSDIR=/home/ubuntu/Stitcher/output/core/strings_output/

grep -Hwrn "$(<$PORTFILE)" "$STRINGSDIR"

