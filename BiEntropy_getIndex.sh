#!/bin/sh
# Script to get the index of molecule with most probable BiEntropy

rm Best_strucures.csv 2> /dev/null
for file in *.dat; do
    extension="${file##*.}"
    filename="${file%.*}"

    echo $filename, $(python BiEntropy_getIndex.py $filename) >> Best_strucures.csv
done