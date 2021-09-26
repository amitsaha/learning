def insertion_sort(alist, order='asc'):
    if not alist:
        return alist
    sorted_list = []
    for num in alist:
        if not sorted_list:
            sorted_list.append(num)
        else:
            # insert the number in the right postition            
            for idx in range(len(sorted_list)):
                if sorted_list[idx] > num:
                    sorted_list.insert(idx, num)
                    break
                elif idx == (len(sorted_list) - 1):
                    sorted_list.append(num)
                else:
                    continue
    return sorted_list


def test_insertion_sort():
    assert insertion_sort([-1]) == [-1]
    assert insertion_sort([]) == []    
    assert insertion_sort([-1, 2, 1, 3, 5]) == [-1, 1, 2, 3, 5]
    assert insertion_sort([-1, -2, -1, -3, 5]) == [-3, -2, -1, -1, 5]
    
