'''
Merge sorted array, A and sorted array, B into the array, A
'''

def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    a.extend(b)
    i = 0
    k = 0
    while k < len_b:
        if a[i] < b[k]:
            i += 1
            continue
        else:
            # shift all elements of a to the right one space
            # and set a[i] = b[k]
            for j in range(i + len_a - 1, i+2):
                print(i, j)
                a[j] = a[j-1]
            a[i] = b[k]
            i += 1
            k += 1

    return a

print(merge([1, 4, 5], [-1, 2, 6]))
