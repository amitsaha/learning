def pset(arr):

    n = len(arr)
    
    for i in range(2**n):
        bit_vector = str(bin(i))[2:]
        indices = [pos for pos, x in enumerate(bit_vector) if x=='1']
        print [arr[int(i)] for i in indices]

arr = [1,2,3]
pset(arr)
