# decimal to binary

def dec2bin(num):

    bin_digits = []
    while num > 0:
        bin_digits.append(str(num%2))
        num = num/2

    return ''.join(bin_digits)

assert dec2bin(5) == str(bin(5)[2:])
