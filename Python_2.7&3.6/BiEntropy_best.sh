#!/bin/sh
#
# 2026-01-30
#
# Run as: sh BiEntropy_best.sh root_system_name number_files_to_process
#         sh BiEntropy_best.sh MBNNB 30
#
# Script to get the files of molecule with most probable BiEntropy
# What the script does:
# 1. Get inside each system folder
# 2. Get inside each concentration folder
# 3. Calculate the entropy of each structure. Create a file named BiEbtropy_system.dat. Move the file to out_BiEntropy folder
# 4. Get inside out_BiEntropy folder and calculate the entropy distribution. Create a file with the most probable structures.
# 5. Copy the structures to out_Best_Structures folder
#
#

# To run BiEntropy, Python2 shoud be used
Pv2="2.7.18"
Pv3="3.10.15"

clear

rm -fr out_BiEntropy 2> /dev/null
mkdir out_BiEntropy

rm -fr out_Best_Structures 2> /dev/null
mkdir out_Best_Structures


filename_root=$1
number_files=$2

for d1 in $filename_root*; do      # System folders
    cd ${d1}
#    echo ${d}
    for d2 in *; do
        cd ${d2}
        echo ${d1} ${d2}
        "${PYENV_ROOT}/versions/$Pv2/bin/python" ../../BiEntropy.sh ${d1} ${d2} $number_files
        mv BiEntropy*.dat ../../out_BiEntropy/
        cd ..
    done
    cd ..
done
#pwd

cd out_BiEntropy/

for file in *.dat; do
   extension="${file##*.}"
   filename="${file%.*}"
   prefix="BiEntropy_"
   foo="${filename#"$prefix"}"
   echo $foo-$("${PYENV_ROOT}/versions/$Pv3/bin/python" ../BiEntropy_getIndex.py $filename).xyz >> Best_structures.csv
done
cd ..

for d1 in $filename_root*; do      # System folders
   cd ${d1}
   while read line; do
   filename=$(echo $line | awk '{printf "%s \n",$1}')
   find -maxdepth 12 -iname ${filename} -exec cp {} ../out_Best_Structures/ \;
   done < ../out_BiEntropy/Best_structures.csv
   cd ..
done
