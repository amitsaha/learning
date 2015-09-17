'''
Given a number of integer intervals, collapse them:

Input: [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
Output:   [(0, 1), (3, 8), (9, 12)]
'''

def collapse_range(slots):

    # order based on the first slot
    ordered_slots = sorted(slots, key=lambda range: range[0])
    merged_slots = []
    i = 0
    j = 0
    while i < len(ordered_slots):
        j = i+1
        l, u = ordered_slots[i]
        while j < len(ordered_slots):
            if ordered_slots[i][1] >= ordered_slots[j][0]:
                u = ordered_slots[j][1]
                i += 1
                j += 1
                continue
            else:
                break
        i = j
        merged_slots.append((l, u))

    return merged_slots

assert collapse_range([(0, 1), (3, 5), (4, 8), (10, 12), (12, 14), (9, 10)]) ==  \
    [(0, 1), (3, 8), (9, 14)]
assert collapse_range([(0, 1), (3, 5), (6, 8), (10, 12), (8, 10)]) ==  \
    [(0, 1), (3, 5), (6, 12)]
assert collapse_range([(0, 1), (3, 5)])  ==  \
    [(0, 1), (3, 5)]
assert collapse_range([(0, 2), (2, 5)])  ==  \
    [(0, 5)]
