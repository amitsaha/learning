filename = 'foo.txt'

# data.sort()
# print data


data = open(filename).readlines()
sorted_data = sorted(data, key = lambda string: string.split()[1])
print sorted_data
