1. Create a folder, ex. myBientropy
2. Copy the functionalized folders to it (myBientropy)
3. Download the files here to it (myBientropy)
4. Execute file **BiEntropy_best.sh**: *sh BiEntropy_best.sh MBNNB 30* (here *30* represents the number of files to be processed).

**Note 1**: These scripts are intended to work with Python > 3.6 (tested with 3.6 and 3.12.6) and [OpenBabel](https://openbabel.org/).
Dependencies install: ´pip install scipy numpy matplotlib´.

**Note 2**: The **BiEntropy.sh** script works with structure file names like: *MBNNB+COOH05-3.xyz*.
            If the names are like *MBNNB+COOH-3.xyz*,  then use rename: `rename s/-/05-/ M*`

Example of folder structure to work with:
```bash
.
├── BiEntropy_best.sh
├── BiEntropy_getIndex.py
├── BiEntropy.sh
├── MBNNB+COOH
│   ├── 05
│   │   ├── MBNNB+COOH05-10.xyz
│   │   ├── MBNNB+COOH05-11.xyz
│   │   ├── MBNNB+COOH05-12.xyz
│   │   ├── MBNNB+COOH05-13.xyz
│   │   ├── MBNNB+COOH05-14.xyz
│   │   ├── MBNNB+COOH05-15.xyz
│   │   ├── MBNNB+COOH05-16.xyz
│   │   ├── MBNNB+COOH05-17.xyz
...
│   │   ├── MBNNB+COOH05-3.xyz
│   │   ├── MBNNB+COOH05-4.xyz
│   │   ├── MBNNB+COOH05-5.xyz
│   │   ├── MBNNB+COOH05-6.xyz
│   │   ├── MBNNB+COOH05-7.xyz
│   │   ├── MBNNB+COOH05-8.xyz
│   │   └── MBNNB+COOH05-9.xyz
│   └── 10
│       ├── MBNNB+COOH10-10.xyz
│       ├── MBNNB+COOH10-11.xyz
│       ├── MBNNB+COOH10-12.xyz
│       ├── MBNNB+COOH10-13.xyz
│       ├── MBNNB+COOH10-14.xyz
│       ├── MBNNB+COOH10-15.xyz
│       ├── MBNNB+COOH10-16.xyz
│       ├── MBNNB+COOH10-17.xyz
...
│       ├── MBNNB+COOH10-3.xyz
│       ├── MBNNB+COOH10-4.xyz
│       ├── MBNNB+COOH10-5.xyz
│       ├── MBNNB+COOH10-6.xyz
│       ├── MBNNB+COOH10-7.xyz
│       ├── MBNNB+COOH10-8.xyz
│       └── MBNNB+COOH10-9.xyz
├── out_Best_Structures *(created folder after running the script)*
│   ├── MBNNB+COOH05-9.xyz
│   └── MBNNB+COOH10-11.xyz
└── out_BiEntropy *(created folder after running the script)*
    ├── Best_structures.csv
    ├── BiEntropy_MBNNB+COOH05.dat
    ├── BiEntropy_MBNNB+COOH05.pdf
    ├── BiEntropy_MBNNB+COOH10.dat
    └── BiEntropy_MBNNB+COOH10.pdf
```
