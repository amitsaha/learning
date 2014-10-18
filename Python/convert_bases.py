"""
binary to decimal
"""
def bin2dec(bin):
    dec = 0
    pos = len(bin) - 1
    for bit in bin:
        dec += int(bit)*2**pos
        pos -= 1
    return dec

assert bin2dec('0')== int(0b0)
assert bin2dec('10')== int(0b10)
assert bin2dec('110')== int(0b110)
assert bin2dec('1111')== int(0b1111)

"""
binary to X base
"""
# def bin2X(bin, b):
    




        
        
    
