# iterate over a list which may contain other lists as items

def iterate(l):
    for item in l:
        if isinstance(item, list):
            iterate(item)
        else:
            print item,

iterate([1,2,3])
print
iterate([1,2,[3,4,5],6,[7,8,9,[10,11,12]]])
    
