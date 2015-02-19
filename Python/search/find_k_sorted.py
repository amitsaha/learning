'''
Given a sorted array of integers, find the number of times
a given number K occurs in the array.
'''

def find_k(arr, item):

    first_occurence = None
    last_occurence = None

    # find the first occurence
    count = 0
    l = 0
    u = len(arr) - 1
    while l <= u:
        mid = int(l + (u-l)/2)
        if arr[mid] == item:
            first_occurence = mid
            if mid == 0:
                break
            if arr[mid-1] < item:
                break
            if arr[mid-1] == item:
                u = mid - 1
        else:
            if arr[mid] < item:
                l = mid + 1
            else:
                u = mid -1

    if first_occurence is None:
        return None

    # find the last occurence
    l = first_occurence
    u = len(arr) - 1
    while l <= u:
        mid = int(l + (u-l)/2)
        if arr[mid] == item:
            last_occurence = mid
            if mid == len(arr) - 1:
                break
            if arr[mid+1] > item:
                break
            if arr[mid+1] == item:
                l = mid + 1
        else:
            if arr[mid] < item:
                l = mid + 1
            else:
                u = mid -1

    if last_occurence is None:
        return None

    return last_occurence - first_occurence + 1


assert find_k([1, 2, 3, 3, 4, 5], 3) == 2
assert find_k([1, 2, 3, 3, 4, 5], 1) == 1
assert find_k([1, 2, 2, 2, 4, 5], 2) == 3
assert find_k([2, 2, 2, 2, 2, 2], 2) == 6
assert find_k([1, 1, 2, 2, 2, 2, 3], 2) == 4
assert find_k([1, 1, 2, 2, 2, 2, 3], 4) == None
