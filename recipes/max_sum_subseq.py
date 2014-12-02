'''
Find the continuous sequence in array with mix of positive and negative integers
with the largest sum: Return the sum
'''

def max_subseq(arr):

    sum = 0
    maxSum = 0
    start = 0
    end = 0
    
    for i in range(1, len(arr)):
        sum += arr[i]
        if maxSum < sum:
            maxSum = sum
        else:
            if sum < 0:
                sum = 0
    return maxSum

print(max_subseq([2, -8, 3, -2, 4, -10]))
