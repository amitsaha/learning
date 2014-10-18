# find whether a number is a palindrome without
# using extra space

import sys
import math

a = int(sys.argv[1])
numdig = int(math.log(a, 10))+1

back = 1
front = numdig 

flag = 1
while back <= front:
    back_dig = int((a/10**(back-1)))%10
    front_dig = int(a/(10**(front-1)))%10
    
    if front_dig != back_dig:
        flag = -1
        break
    #print front, back
    back += 1 
    front -= 1

if flag == -1:
    print 'Not a palindrome'
else:
    print 'Palindrome'

    
