"""
String matcher using regex
"""
import re
def match(pattern, string):
    return bool(re.compile(pattern).match(string))

print match('ab*', 'abba')
print match('ab.a', 'a')
   
