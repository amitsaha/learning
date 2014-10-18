def find_leftmost(arr, item):
    
    start = 0
    end = len(arr) - 1

    found = None
    while start <= end:
        mid = start + (end-start)/2
        
        if arr[mid] == item:
            found = mid

        if arr[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
            
    return found

arr = [-1, 1, 1, 2, 2, 3]
assert find_leftmost(arr, 1) == 1
assert find_leftmost(arr, -1) == 0
assert find_leftmost(arr, 2) == 3
assert find_leftmost(arr, 3) == 5    
            
