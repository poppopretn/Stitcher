#!/bin/bash
# Script to compare process list and file list.
# File paths - Amend file paths accordingly to where the files are stored.

PROCESSLIST=/home/ubuntu/Stitcher/output/core/processlist.txt
FILELIST=/home/ubuntu/Stitcher/output/core/filelist.txt

while read PROCESSES
do
  grep "$PROCESSES" $FILELIST 2>/dev/null
done < $PROCESSLIST
