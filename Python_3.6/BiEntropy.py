#!/usr/bin/env python3
# Python 3.6 compatible
# 2026-01-30
#
# Run as:
#   python BiEntropy.py MBNNB+COOH 05 5
#
# Structure file names like: MBNNB+COOH05-3.xyz
#
# If names are like MBNNB+COOH-3.xyz, use rename: rename s/-/05-/ M*
#

import glob
import os
import sys
import subprocess
import shutil
import itertools

from bientropy import tbien
from bitstring import BitArray, Bits

# ---------------------------------------------------------------------------
# readwords: replaces the Python 2 itertools.imap version
# Reads one byte at a time and yields non-whitespace tokens
# ---------------------------------------------------------------------------
def readwords(mfile):
    """
    Generator that yields non-whitespace string tokens from a file object,
    reading one byte at a time. Replaces the Python 2 itertools.imap approach.
    """
    def read_bytes(f):
        """Inner generator: yields single characters until EOF."""
        while True:
            c = f.read(1)
            if not c:        # EOF reached
                break
            yield c

    byte_stream = itertools.groupby(read_bytes(mfile), str.isspace)
    return ("".join(group) for pred, group in byte_stream if not pred)


# ---------------------------------------------------------------------------
# Argument validation
# ---------------------------------------------------------------------------
if len(sys.argv) < 4:
    print("Usage: python BiEntropy.py <base_filename> <percentage> <number_of_files>")
    print("  Example: python BiEntropy.py MBNNB+COOH 05 5")
    sys.exit(1)

file_name    = sys.argv[1]   # e.g. MBNNB+COOH  — base filename
perc         = sys.argv[2]   # e.g. 05, 10, 15, 20, 25
number_files = sys.argv[3]   # total number of .xyz files to process

# ---------------------------------------------------------------------------
# File extension definitions
# ---------------------------------------------------------------------------
mol_ext_in   = '.xyz'    # input molecular structure files
bfgp_ext_out = '.bfgp'  # binary fingerprint output
hfgp_ext_out = '.hfgp'  # hex fingerprint output

# ---------------------------------------------------------------------------
# Open output data file
# e.g. BiEntropy_MBNNB+COOH05.dat
# ---------------------------------------------------------------------------
file_data_name = f'BiEntropy_{file_name}{perc}.dat'
file_data = open(file_data_name, 'w')

# ---------------------------------------------------------------------------
# Main processing loop
# ---------------------------------------------------------------------------
with open(os.devnull, 'w') as FNULL:
    for i in range(1, int(number_files) + 1):

        file_in   = f'{file_name}{perc}-{i}{mol_ext_in}'   # e.g. MBNNB+COOH05-1.xyz
        file_hfgp = f'{i}{hfgp_ext_out}'                    # e.g. 1.hfgp
        file_bfgp = f'{i}{bfgp_ext_out}'                    # e.g. 1.bfgp

        # --- Generate hex fingerprint with obabel ---
        args = f'obabel {file_in} -ofpt -xfECFP4 -Ofinger.tmp'
        ret = subprocess.call(args.split(), stdout=FNULL, stderr=subprocess.STDOUT)

        if ret != 0:
            print(f'[WARNING] obabel failed for: {file_in} (exit code {ret}), skipping.')
            continue

        # --- Validate finger.tmp was created and is non-empty ---
        if not os.path.exists('finger.tmp') or os.path.getsize('finger.tmp') == 0:
            print(f'[WARNING] finger.tmp is empty or missing for: {file_in}, skipping.')
            continue

        # --- Remove obabel header line, write remainder to .hfgp ---
        with open('finger.tmp', 'r') as source_file:
            source_file.readline()          # discard first header line
            content = source_file.read().strip()

        if not content:
            print(f'[WARNING] No fingerprint content after header in finger.tmp for: {file_in}, skipping.')
            continue

        with open(file_hfgp, 'w') as target_file:
            target_file.write(content)

        # --- Build binary fingerprint string from hex tokens ---
        binary_fingerprint = ''
        with open(file_hfgp, 'r') as f:
            for word in readwords(f):
                word = word.strip()
                if not word:
                    continue
                try:
                    w = BitArray(f'0x{word}')
                    binary_fingerprint += w.bin
                except Exception as e:
                    print(f'[WARNING] Skipping invalid hex token "{word}": {e}')
                    continue

        # --- Guard against empty fingerprint ---
        if not binary_fingerprint:
            print(f'[WARNING] Empty binary fingerprint for: {file_in}, skipping.')
            continue

        print(f'[INFO] File {i}: fingerprint length = {len(binary_fingerprint)} bits')

        # --- Save binary fingerprint to .bfgp ---
        with open(file_bfgp, 'w') as fpou:
            fpou.write(binary_fingerprint)

        # --- Compute TBiEntropy ---
        # tbien() requires a bitstring.Bits object, NOT a plain str
        try:
            bits_fp = Bits(bin=binary_fingerprint)
            tb = tbien(bits_fp)
        except Exception as e:
            print(f'[ERROR] tbien() failed for file {i}: {e}')
            continue

        line = f'{i} {tb}\n'
        file_data.write(line)
        print(f'[INFO] File {i}: TBiEntropy = {tb}')

file_data.close()

# ---------------------------------------------------------------------------
# Cleanup all temporary files
# ---------------------------------------------------------------------------
for pattern in ('*.bfgp', '*.hfgp', '*.tmp'):
    for temp_file in glob.glob(pattern):
        os.remove(temp_file)

print('[DONE] BiEntropy calculation complete.')
