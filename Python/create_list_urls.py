# create a file with a billion URLs

import random

with open('urls.txt', 'w') as f:
    for i in xrange(1, 10**3):
        f.write('www.url%d.com\n' % random.randint(1, 10**3))

