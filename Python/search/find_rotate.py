"""
Rotated binary search
"""

def find_rotate(numbers, item):
    a = 0
    b = len(numbers)-1
    m = (a+b)/2

    while a<=b:
        m = (a+b)/2
        if item == numbers[m]:
            return m

        if numbers[a] < numbers[m]:
            # left is sorted
            if item >= numbers[a] and item < numbers[m]:
                b = m-1
            else:
                a = m+1
        else:
            # right is sorted
            if item > numbers[m] and item <= numbers[b]:
                a = m+1
            else:
                b = m-1

numbers = [10,11,0,1,2,3]
print find_rotate(numbers, 10)      
print find_rotate(numbers, 3)
print find_rotate(numbers, 11)
