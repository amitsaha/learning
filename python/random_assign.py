'''
Assume a container of capacity 10. Assume 10 boxes each marked
for a container. Use MC sampling to match each box to a container.
What is the average number of correct matches over say 100000 
simulations?
'''

import random
def assign():
    boxes = [i for i in range(1, 11)]
    # shuffle the box and see which index and the number in in matches
    # this is our box assignment
    random.shuffle(boxes)
    c = 0
    for pos, elem in enumerate(boxes):
        if elem == pos:
            c += 1
    return c

if __name__ == '__main__':
    print(sum([assign() for i in range(100000)])/100000)
