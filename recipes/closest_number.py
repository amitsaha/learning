'''
Closest number to a given number in a sorted list of numbers
'''
# linear: also works for an unsorted list
def closest_number(arr, item):

    diff = abs(arr[0] - item)
    for n in arr:
        if abs(n-item) <= diff:
            diff = abs(n-item)
            closest = n

    return closest

# binary search
def closest_number_2(arr, item):

    l = 0
    u = len(arr) - 1

    while l <= u:
        mid = (l+u)/2
        if abs(arr[mid] - item) < abs(arr[u] - item):
            u = mid
        else:
            l = mid + 1
    return arr[u]

print(closest_number([1, 5, 7, 10], 4))
print(closest_number([1, 4, 5, 7, 10], 4))
print(closest_number([1, 4, 5, 7, 10], 11))

print(closest_number_2([1, 5, 7, 10], 4))
print(closest_number_2([1, 4, 5, 7, 10], 4))
print(closest_number_2([1, 4, 5, 7, 10], 11))
print(closest_number_2([1, 4, 5, 7, 10], 8))
