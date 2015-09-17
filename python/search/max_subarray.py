# Linear scan through an array to find the sum of 
# the maximum sub array
# http://www.cs.waikato.ac.nz/Teaching/COMP317B/Week_1/AlgorithmDesignTechniques.pdf

def max_subarray(arr):
    max_sofar = 0
    max_endinghere = 0

    for i in range(len(arr)):
        max_endinghere = max(0, max_endinghere + arr[i])
        max_sofar = max(max_sofar, max_endinghere)

    return max_sofar


print max_subarray([1,-1,0,1,2])
