'''
Generate a random number of length, N and all digits
are unique
'''
from __future__ import print_function
import random
from collections import OrderedDict

# keep generating till all are unique
# This is a brute force approach where I store the digits generated
# so far in a OrderedDict and if the next random number is already
# there, i ignore it.
def randN(n):
    assert n <= 10
    digits = OrderedDict()
    while len(digits) < n:
        d = random.randint(0, 9)
        if d == 0 and not digits.keys():
            continue
        else:
            if not digits.get(str(d), None):
                digits[str(d)] = 1
    return int(''.join(digits.keys()))

# and a simpler approach
# http://codereview.stackexchange.com/a/69799/58086
def randN1(n):
    assert n<=10
    digits = list(range(10))
    while digits[0] == 0:
        random.shuffle(digits)
    return int(''.join(str(d) for d in digits[:n]))

def _assert(randi, n):
    assert len(str(randi)) == n
    assert len(set(str(randi))) == n

for _ in range(100000):
    _assert(randN(10), 10)
    _assert(randN(1), 1)
    _assert(randN(5), 5)

    _assert(randN1(10), 10)
    _assert(randN1(1), 1)
    _assert(randN1(5), 5)
