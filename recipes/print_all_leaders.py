'''
Print all leaders from an array:

A leader is an element for which all the numbers to it's right are
either equal or less than it
'''

from __future__ import print_function

def find_leaders(arr):
    max = arr[-1]

    for elem in arr[::-1]:
        if elem >= max:
            print(elem)
            max = elem

find_leaders([10, 2, 3, -1, -2, 5, 4, 3, 2 ,1])
find_leaders([10, 2, 3, 5, 3, 2 ,1])
