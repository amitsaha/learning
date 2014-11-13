'''
Check whether a string, t is a sub-sequence of string, s:

Reference: http://www.ics.uci.edu/~eppstein/161/960229.html
'''
def check_subsequence(s, t):
    t_pos = 0
    for i in range(len(s)):
        if t_pos < len(t):
            if s[i] == t[t_pos]:
                # continue moving right of the smaller string
                t_pos += 1
                continue
    # we have scanned the entire string, s
    if t_pos == len(t):
        return True
    else:
        return False

# test data
assert check_subsequence('nematode knowledge', 'nano')
assert not check_subsequence('nematodee', 'nano')
assert check_subsequence('nano', 'nano')
assert check_subsequence('noanooo', 'nano')
assert check_subsequence('noop', 'no')
assert check_subsequence('abba', 'aba')
assert check_subsequence('atgcat', 'cat')
