import difflib


def isjunk(x):
    return x in ' \t'

"""
Ratcliff-Obershelp algorithm
- Doesn't yield minimal edit distances
- Worst case: quadratic
- Best case: linear
"""

def find_edit_distance(s1, s2):
    
    s = difflib.SequenceMatcher(s1, s2)
    changes = [x for x in s.get_opcodes() if x[0] != 'equal']
    
    if len(changes) == 0 or len(changes) > 1:
        return len(changes)
    else:
        diff1 = changes[0][3] - changes[0][1]
        diff2 = changes[0][4] - changes[0][2]

        if diff1 <=1 and diff2 <= 1:
            return 1
        else:
            return changes
        
print 'Hell -> Hello', find_edit_distance('Hell', 'Hello ')
print 'Hell -> Hello', find_edit_distance('Hell', 'Hello\t')
