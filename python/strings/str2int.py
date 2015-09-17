# string to integer

def myint(string):
    
    if string[0] == '-':
        neg = True
        string = string[1:]
    else:
        neg = False
    
    num = 0
    for s in string:
        num *= 10
        num += int(s)

    if neg:
        num = -1*num
    
    return num

print myint('123')
print myint('-123')
print myint('1232731723')
