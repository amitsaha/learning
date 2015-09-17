'''
Find the minimum number of operations to reduce a given number, N
to 1 using only the following allowed operations:

1. Subtract 1 from it
2. If it is even, divide by 2
3. If it is divisible by 3, divie by 3

This uses dynamic programming technique to solve the above problem since
the problem exhibits both optimal substructure and overlapping subproblems

Reference: http://www.codechef.com/wiki/tutorial-dynamic-programming
'''

def find_steps_to_1(N):
    if N <= 1:
        return 0
    else:
        # "Array": [0, 0, .. N], [0] is unused
        steps = [0*i for i in range(0, N+1)]
        # trivial step, number of steps for 1 = 0
        steps[1] = 0
        for i in range(2, N+1):
            steps[i] = steps[i-1] + 1
            if i%2 == 0:
                steps[i] = min(steps[i], 1 + steps[int(i/2)])
            if i%3 == 0:
                steps[i] = min(steps[i], 1 + steps[int(i/3)])
    return steps[N]

# test data
assert find_steps_to_1(1) == 0
assert find_steps_to_1(3) == 1
assert find_steps_to_1(4) == 2
assert find_steps_to_1(7) == 3
