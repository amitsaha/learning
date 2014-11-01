'''
Find the numbers which occur even number of times
'''

arr = [1, 2, 2, 5, 7, 9, 3, 3, 1, 10, 9, 10, 10, 9]

# naive
count = {}
for item in arr:
    count[item] = count.get(item, 0) + 1
for k, v in count.iteritems():
    if v%2==0:
        print k
