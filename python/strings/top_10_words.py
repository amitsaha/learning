import collections
with open('words.dat') as f:
    words = f.readlines()

w = collections.Counter(words)
print w.most_common(10)

