#!/bin/bash
# Script to diff file hashes between core evidence and baseline evidence.
# File paths - Amend file paths accordingly to where the files are stored.

COREFILEHASHES=/home/ubuntu/Stitcher/output/core/filehash.txt
BASELINEFILEHASHES=/home/ubuntu/Stitcher/output/baseline/filehash.txt

diff $COREFILEHASHES $BASELINEFILEHASHES
