# closest distance between two equal strings

from collections import OrderedDict

def closest(arr):

    d = OrderedDict()
    dist = len(arr) - 1
    for i, s in enumerate(arr):
        indices = d.get(s, None)
        if not indices:
            d[s] = [i]
        else:
            if len(indices) > 1:
                d1 = abs(d[s][1] - d[s][0])
                d2 = abs(i - d[s][0])
                d3 = abs(i - d[s][1])
                if d2 < d1:
                    d[s][1] = i
                if d3 < d1:
                    d[s][0] = i
            else:
                d[s].append(i)
    print(d)

closest(["All", "work", "and", "no", "play", "makes", "for",
         "no", "fun", "and", "no", "results", "no", "life"])
