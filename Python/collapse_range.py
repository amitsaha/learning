'''
Input: [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
Output:   [(0, 1), (3, 8), (9, 12)]
'''

def collapse_range(slots):
    
    hours = []
    for s in slots:
        hours.append(range(s[0], s[1]+1))
    all_hours = list(set(hours[0]).union(*hours[1:]))

    start = all_hours[0]
    for pos, item in enumerate(all_hours):
        if pos < len(all_hours)-2 and item + 1 == all_hours[pos+1]:
            continue
        else:
            print start, item
            start = all_hours[pos+1]

collapse_range([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    
    
