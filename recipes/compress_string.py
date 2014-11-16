'''
Input String = "ABBCDEFGGGGGGGGHHXX..<20 more X>..XYY..." 
Expected output = "A1B2C1D1E1F1G8H2X23Y2..."
'''

from __future__ import print_function

def compress(input_string):
    cur = input_string[0]
    compressed = [cur]
    count = 1
    pos = 1
    while pos < len(input_string):
        if cur == input_string[pos]:
            count += 1
        else:
            compressed.append(str(count))
            cur = input_string[pos]
            compressed.append(cur)
            count = 1
        pos += 1
    compressed.append(count)
    
    return compressed

print(compress('AABB'))
print(compress('AABBCCCCDDDXX'))
