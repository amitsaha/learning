'''
Counting sort implementation: O(n)
Example: sort an array containing employee ages
http://en.wikipedia.org/wiki/Counting_sort
'''

def sort_ages(arr):

    max_age = 99
    age_count = {}
    # O(n) time complexity
    # storage space for the dictionary: 100 max.
    for i in arr:
        age_count[i] = age_count.get(i, 0) + 1
    # Print them
    for i in range(0, max_age):
        if age_count.get(i, None):
            for j in range(age_count[i]):
                print(i)

# test
sort_ages([56, 34, 50, 27, 28, 27])
