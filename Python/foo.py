import os

def walk(d):
    for f in os.listdir(os.path.abspath(d)):
        if os.path.isdir(os.path.abspath(f)):
            # walk again
            walk(os.path.abspath(f))
        else:
            # file
            print 'f: ' + f
            pass

walk('.')
    
    
