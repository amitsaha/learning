'''
Fibonacci series using dynamic programming technique
'''
from __future__ import print_function
# space optimized version
# http://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def fib(n):
    series = [0, 1]
    for i in range(2, n):
        next = series[0] + series[1]
        print(next)
        series.pop(0)
        series.append(next)

fib(100)
