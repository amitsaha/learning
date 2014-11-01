#Given a large array of unsigned ints, quickly find two who's sum is equal to x and print the indices of the ints.

#[ 1, 2, 3, 4, 5 ] | 7 | 2, 3


def find_indices_sum(arr, x):
    # create the dictionary
    mydict = {}
    for idx, item in enumerate(arr):
        found_idx = mydict.get(x-item, None)
        if found_idx:
                print idx, found_idx
                break
        else:
                mydict[item] = idx
    
                
            
        
arr = [1, 2, 3, 4, 5]
x = 7
find_indices_sum(arr, x)

arr = [1, 2, 3, 4, 5, 5]
x = 10
find_indices_sum(arr, x)


