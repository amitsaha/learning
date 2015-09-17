def bsearch(arr, item):
    
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end-start)/2
        if arr[mid] == item:
            return mid
        
        if arr[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    
    return None


arr = [1,2,3,10,11]
print bsearch(arr, 2)
