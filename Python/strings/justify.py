"""
Justify a paragraph
"""


def justify(p):
    lines = p.splitlines()
    max_length = max([len(line) for line in lines])
    
    for line in lines:
        if len(line) != max_length:
            words = line.split()
            whitespaces = len(words) - 1
            for w in words:
                print w+' '*int(((max_length - len(line))/(whitespaces*1.0))),
            print
                
        else:
            print line

justify('''
This is a line of text
This is a second line
Third line
''')
        
