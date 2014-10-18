from collections import Counter

def top10(f):
    
    with open(f) as fobj:
        words = fobj.read().split()
        
    c = Counter(words)
    print c.most_common(10)

top10('file.dat')

