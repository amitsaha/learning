"""
Radix sort implementation

Example:

120 119 98 78

digit:1

120 98 78 119

digit:2

119 120 78 98

digit:3

78 98 119 120
"""

def rsort(numbers):
    passes = max([len(str(num)) for num in numbers])
    for p in range(1,passes+1):
        buckets = [[] for _ in range(10)]
        for n in numbers:
            digit = (n/10**(p-1))%10
            buckets[digit].append(n)
        print buckets
        numbers = []
        for b in buckets:
            numbers.extend(b)

    return numbers

numbers = [120, 119, 98, 78]
print rsort(numbers)
numbers = [120, 119, 98, 78, 1]
print rsort(numbers)

