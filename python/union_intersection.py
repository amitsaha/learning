
#Implement the intersection and union operation on sorted lists. The result of the intersect and union should be another sorted list. Once we have the basic intersection and union #algorithms, parallelize them.

# Example data:
# 3, 4, 5, 10
# 4, 7, 10

# -10, 11, 100, 101
# -5, -4, 11, 100

# 10, 11, 12, 13
# 1, 2, 3, 4

def intersection(list1, list2):
    
    # set up a dummy dictionary for list2
    # O(n)
    list2 = {k:1 for k in list2}
    
    # find the intersection
    # O(min(m, n)) space
    intersect = []
    
    # O(m)
    for n in list1:
        # O(1) look up
        if n in list2:
            intersect.append(n)
            
    return intersect
    
def union(list1, list2):
    
     union_list = {}
     
     p1 = 0
     p2 = 0
     
     # O(min(m,n)
     while p1 < len(list1) and p2 < len(list2):
         if list1[p1] < list2[p2]:
             if list1[p1] not in union_list:
                   union_list[list1[p1]] = 1                   
              p1 += 1        
                   
         else:
             if list2[p2] not in union_list:
                    union_list[list1[p1]] = 1   
                   union_list.append(list2[p2])
             p2 += 1         
             
    # for list1
    for i in range(p1, len(list1)):
        if list1[p1] not in union_list:
            union_list.append(list1[p1])    
    # for list2
    for i in range(p2, len(list2)):
        if list2[p2] not in union_list:
            union_list.append(list2[p2])
            
    return union_list
    
