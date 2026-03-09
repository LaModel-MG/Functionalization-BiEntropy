1. Create a folder, ex. myBientropy
2. Copy the functionalized folders to it (myBientropy)
3. Download the files here to it (myBientropy)
4. Execute file **BiEntropy_best.sh**: *sh BiEntropy_best.sh MBNNB 30* (here *30* represents the number of files to be processed).

**Note 0**: These scripts are intended to work with [PYENV](https://realpython.com/intro-to-pyenv/) (for Python installation/configuration) and [OpenBabel](https://openbabel.org/).

**Note 1**: These files where made to be used with two Python versions at the same time, *2.7.18* for **BiEntropy.sh** and *3.10.15* for **BiEntropy_getIndex.py**.
In this case, the Python control version is done using PyEnv (Info to setup/use [here](https://realpython.com/intro-to-pyenv/)).

**Note 2**: The **BiEntropy.py** script works with structure file names like: *MBNNB+COOH05-3.xyz*.
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
