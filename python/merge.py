def merge(list1, list2):
    c1 = 0
    c2 = 0
    
    merged = []      
    
    while c1 < len(list1) and c2 < len(list2):
        
        if list2[c2] > list1[c1]:
            merged.append(list2[c2])
            c2 +=1
        else:
            merged.append(list1[c1])
            c1 += 1
            
    if c1 == len(list1):
        merged.extend(list2[c2:])
          
    if c2 == len(list2):
        merged.extend(list1[c1:])
        
    print merged

merge([4, 2, 1], [7, 6, 5, 3])
merge([4, 2, 1,0], [7, 6])
        

