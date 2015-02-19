'''
string to integer
'''

def atoi(s):
    
    start_pos = 0
    negative = False
    if s[0] == '-':
        start_pos = 1
        negative = True
       
    number = 0
    for i in range(start_pos, len(s)):
        number = number*10 + int(s[i])
    if negative:
        return -number
    else:
        return number

assert atoi('1234') == 1234
assert atoi('-1234') == -1234
   
