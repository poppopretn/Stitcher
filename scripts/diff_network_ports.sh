#!/bin/bash
# Script to diff network ports between core evidence and baseline evidence.
# File paths - Amend file paths accordingly to where the files are stored.

COREPORTLIST=/home/ubuntu/Stitcher/output/core/topTCPports.txt
BASELINEPORTLIST=/home/ubuntu/Stitcher/output/baseline/topTCPports.txt

diff $COREPORTLIST $BASELINEPORTLIST
