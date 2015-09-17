"""
Run-Length Encoding and decoding
"""

def rld(s):

    characters = [c for i,c in enumerate(s)  if i%2 != 0]
    rept = [r for i, r in enumerate(s) if i%2 == 0]
    for r,c in zip(rept, characters):
        print c*int(r),
    print

def rle(s):
    s += ' '
    current = s[0]
    num = 1
    enc = ''
    for pos, c in enumerate(s[1:]):
        if c==current:
            num+=1
        else:
            enc += str(num) + current
            current = c
            num = 1
    return enc

rld(rle('aaaabccaa'))
rld(rle('aaaabccd'))
