def merge(*args):
    '''
    Merge elements in N sorted lists
    and return a single sorted list
    '''
    # final merged list
    final = []
    while any(args):
        least = [(i, l[0]) for i, l in enumerate(args) if l]
        # Insert the smallest of these in the final list
        least.sort(key=lambda x: x[1])
        list_num, elem = least[0]
        final.append(elem)
        # pop the element of the list from which the
        # smallest element came
        args[list_num].pop(0)

    return final

# test data
l1 = [1, 2, 3, 4]
l2 = [-100, 6, 7, 8]
l3 = [-95, -94, -93, -92, -91]
assert sorted(l1+l2+l3)==merge(l2, l3, l1)

# test data
l1 = [-200, 2, 3, ]
l2 = [-100, 6, 7, 8]
l3 = [-95, -94, -93, -92, -91]
assert sorted(l1+l2+l3)==merge(l2, l3, l1)

