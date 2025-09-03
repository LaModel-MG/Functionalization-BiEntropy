#!/usr/bin/python2.7.18
import glob, os
import sys
import subprocess
import shutil
from bientropy import bien, tbien
from bitstring import Bits
from bitstring import BitArray, BitStream

import itertools
#itertools.imap = lambda *args, **kwargs: list(map(*args, **kwargs))    #Python3?

def readwords(mfile):
    byte_stream = itertools.groupby(
        itertools.takewhile(lambda c: bool(c),
            itertools.imap(mfile.read,
                itertools.repeat(1))), str.isspace)

    return ("".join(group) for pred, group in byte_stream if not pred)


file_name = sys.argv[1] #'BN+OH-N-'  # Base filename of molecular input files
perc =  sys.argv[2] #Percentage: 05, 10, 15, 20, 25
number_files = sys.argv[3]  #Number of files to process
#file_data_name = 'BiEntropy_' + file_name + '-' + perc + '.dat'
file_data_name = 'BiEntropy_' + file_name + perc + '.dat' # g-C3N4+OH05-541.xyz
file_data = open(file_data_name, 'w')
mol_ext_in = '.xyz'     # Extension of molecular input files

bfgp_ext_out = '.bfgp'  # Extension for vile with binary fingerprint
hfgp_ext_out = '.hfgp'  # Extension for vile with binary fingerprint
FNULL = open(os.devnull, 'w')
for i in range(1,int(number_files)+1):
#    print (i)
    file_in = file_name + perc + '-' + str(i) + mol_ext_in
#    print file_in
    file_hfgp = str(i) + hfgp_ext_out
    file_bfgp = str(i) + bfgp_ext_out
    # Create hexa fingerprint using obabel
    args = 'obabel ' + file_in + ' -ofpt -xfECFP4 -Ofinger.tmp'
    subprocess.call(args.split(' '), stdout=FNULL, stderr=subprocess.STDOUT)
    # Removing the first line in finger.tmp
    source_file = open('finger.tmp', 'r')
    source_file.readline()
    target_file = open(file_hfgp, 'w')
    shutil.copyfileobj(source_file, target_file)
    target_file.close()
    # Calculatind BiEntropy
    binary_fingerprint=''
    with open(file_hfgp, 'r') as f:
        for word in readwords(f):
            k=word
            w=BitArray('0x'+k)
            binary_fingerprint = binary_fingerprint + w.bin;

    fpou = open(file_bfgp, 'w')
    fpou.write(binary_fingerprint)
    fpou.close()
    tb = tbien(binary_fingerprint)
    args = str(i) + ' ' + str(tb) + '\n'
    file_data.write(args);

file_data.close()
files_delete = glob.glob('*.bfgp')
for file in files_delete:
    os.remove(file)
files_delete = glob.glob('*.hfgp')
for file in files_delete:
    os.remove(file)
files_delete = glob.glob('*.tmp')
for file in files_delete:
    os.remove(file)
