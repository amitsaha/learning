import os
from collections import defaultdict
# find duplicate files
for dirpath, dirname, files in os.walk('.'):
    if dirpath == '.':
        f_contents_hash = defaultdict(list)
        for f in files:
            f_hash = hash(open(f).read())
            f_contents_hash[f_hash].append(f)

        duplicates = [v for v in f_contents_hash.values() if len(v) > 1]
        print duplicates
