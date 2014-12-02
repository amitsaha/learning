'''
You are given an array of 1's 2's and 3's. Sort this list so the 1's are first, the 2's come second, and the 3's come third. 
Ex: 
Input [1, 3, 3, 2, 1] 
Output [1, 1, 2, 3, 3] 

Question from: 
https://sites.google.com/site/spaceofjameschen/home/sort-and-search/dutch-national-flag
Ref: http://en.wikipedia.org/wiki/Dutch_national_flag_problem
'''

from __future__ import print_function

def rearrange(arr):

    lo = 0
    while arr[lo] == 1 and lo < len(arr):
        lo += 1

    gt = len(arr) - 1
    while arr[gt] == 3 and gt >= 0:
        gt -= 1

    mid = lo    
    while mid <= gt:
        if arr[mid] == 1:
            arr[lo], arr[mid] = arr[lo], arr[mid]
            lo += 1
            mid += 1
        elif arr[mid] == 2:
            mid += 1
        else:
            arr[mid], arr[gt] = arr[gt], arr[mid]
            gt -= 1

    return arr

print(rearrange([1, 2, 2, 1, 3, 2]))
    
