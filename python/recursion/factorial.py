import math
def factorial(n):
    
    if n == 0:
        return 1
    return n*factorial(n-1)

assert factorial(5) == math.factorial(5)
assert factorial(10) == math.factorial(10)
