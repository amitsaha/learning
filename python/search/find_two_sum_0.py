"""
Find two numbers with sum closest to 0
"""

def approach1(numbers):
    
    # sort - O(nlogn)
    numbers.sort()
    l = 0
    r = len(numbers)-1
    # sum
    s, pos_l, pos_r, = numbers[l] + numbers[r], -1,-1
    # O(n)
    while l<r:
        cur_sum = numbers[l] + numbers[r]
        if abs(cur_sum) <= s:
            s = cur_sum
            pos_l, pos_r = l, r

        if cur_sum < 0:
            l +=1
        else:
            r -=1

    return numbers[pos_l], numbers[pos_r]

print approach1([1,3,10])
print approach1([1,3,10,100])
print approach1([-1, 1,3,10,100])
