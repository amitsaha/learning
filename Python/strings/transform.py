import difflib

def transform(s1, s2):
    print 'To transform {0} to {1}'.format(s1, s2)
    s = difflib.SequenceMatcher(None, s1, s2)
    
    for t in s.get_opcodes():
        print t

transform('hell', 'hello')
transform('house', 'hell')
transform('linux', 'windows')
transform('hrose', 'house')
transform('hrose', 'horse')

