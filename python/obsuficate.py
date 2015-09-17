import os
import re

pattern_email =  re.compile('[a-z]*@[a-z]*\\.[a-z]*')
start_here = '.'

for dirpath, dirname, files in os.walk(start_here):
    for f in files:
        if os.path.splitext(f)[1] == '.html':
            with open(f) as fobj:
                lines = fobj.readlines()
                                
                for line in lines:
                    #assuming that the occurence of a an @ in a word is an email address
                    words = line.split()
                    for w in words:
                        if pattern_email.match(w):
                            print ''.join(['XXX','@', w.split('@')[1]])
