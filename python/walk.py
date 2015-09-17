import os

def cleanup(dirname, numdays):

    for f in os.listdir(dirname):
        
        if os.path.isdir(f):
            cleanup(dirname=os.path.abspath(f), numdays=numdays)
        else:
            print f

cleanup('/home/gene', 10)

