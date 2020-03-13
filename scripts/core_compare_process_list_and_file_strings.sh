#!/bin/bash
# Script to compare process list and file strings.
# File paths - Amend file paths accordingly to where the files are stored.

PROCESSLIST=/home/ubuntu/Stitcher/output/core/processlist.txt
STRINGSDIR=/home/ubuntu/Stitcher/output/core/strings_output/

while read PROCESSES
do
  grep -wnr "$PROCESSES" $STRINGSDIR
  done < $PROCESSLIST
