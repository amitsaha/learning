# find the N largest files in the current directory
import os
N = 2
for dirpath, dirnames, fnames in os.walk('.'):
    if dirpath == '.':
        fnames_sorted = sorted(fnames,
                               key = lambda f: os.path.getsize(f), reverse=True)
        print fnames_sorted[:N]

