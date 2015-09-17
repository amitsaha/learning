# Dump a nested list
def unroll(lst):
    for item in lst:
        if isinstance(item, list):
            unroll(item)
        else:
            print(item)
    return

unroll([1, 2, 3])
unroll([1, 2, 3, [1, [1, 2, 3], 2, 3]])
