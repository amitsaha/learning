import glob
import sys
import os

def ls(path):

    if '*' in path:
        for f in glob.iglob(path):
            print f
    else:
        if os.path.isfile(path):
            print path
        else:
            for d in os.listdir(path):
                print d

ls(sys.argv[1])
