"""
Remove duplication characters from a string
"""

def undup(s):
    return ''.join([c for c in set(s)])

print undup('abba')
