import os
from threading import Thread


def threaded_io():
    print 'Thread running'
    print 'Thread exiting'


print 'PID: ', os.getpid()
t = Thread(target=threaded_io)
t.start()

