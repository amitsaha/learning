""" 
Reverse a string in place
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
    

print rev('foobar')
#print rev('foobar foobar')

