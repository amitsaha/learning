def search_equal_greater(arr, target):
    
    l = 0
    u = len(arr) - 1
    
    while l < u:
        mid = (l+(u-l)/2)
        
        if arr[mid] >= target:
            return mid
        
        l = mid+1

arr = [3, 4, 5, 10, 11]
print search_equal_greater(arr, 4)
