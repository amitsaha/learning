'''
Is a string a palindrome?
'''

def ispalin(s):
    start = 0
    end = len(s)-1

    while start <= end:
        if s[start] == s[end]:
            start +=1
            end -= 1
            continue
        else:
            print 'Not palindrome'
            return

    print 'Palindrome'

ispalin('abba')
ispalin('aabbaa')

    
        
