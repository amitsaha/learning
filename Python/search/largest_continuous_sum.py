'''
Find the largest continuous sum
'''

def largest_cont_sum(arr):
    if len(arr) == 0:
        return 0
    cur_sum = arr[0]
    max_sum = arr[0]
    for item in arr[1:]:
        cur_sum = max(cur_sum+item, item)
        if cur_sum >= max_sum:
            max_sum = cur_sum

    return max_sum  
