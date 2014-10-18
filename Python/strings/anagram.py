""" 
Anagram detection
"""

def check_anagram(s1, s2):
    if len(s1) != len(s2) or not s1 or not s2:
        return False

    return sorted(s1) == sorted(s2)

print check_anagram('abba', 'bbaa')
