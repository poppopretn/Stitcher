#!/bin/bash
# Script to diff file list between core evidence and baseline evidence.
# File paths - Amend file paths accordingly to where the files are stored.

COREFILELIST=/home/ubuntu/Stitcher/output/core/filelist.txt
BASELINEFILELIST=/home/ubuntu/Stitcher/output/baseline/filelist.txt

diff $COREFILELIST $BASELINEFILELIST
