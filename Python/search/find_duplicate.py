# Linear

def find_duplicate(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return arr[i]
    
arr = [1,2,3,4,5,6,6]

print find_duplicate(arr)



