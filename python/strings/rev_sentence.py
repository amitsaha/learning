""" 
Reverse a sentence in place
"""

def rev(s):
    start = 0
    end = len(s)-1
    s = list(s)
    
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)
    
# first reverse
s = rev('this is the last word')
# reverse only the words
words = s.split()
for i, w in enumerate(words):
    words[i] = rev(w)

print ' '.join(words)
