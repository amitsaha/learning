- https://docs.python.org/2/library/bisect.html


>>> import bisect
>>> l = [1, 2, 3, 10, 11]
>>> 
>>> toinsert = 5
>>> bisect.bisect(l, toinsert)
3
>>> bisect.bisect_left(l, toinsert)
3
>>> toinsert = 3
>>> bisect.bisect(l, toinsert)
3
>>> bisect.bisect_left(l, toinsert)
2
>>> 
>>> 
>>> bisect.insort(l, toinsert)
>>> l
[1, 2, 3, 3, 10, 11]
>>> toinsert = 5
>>> bisect.insort(l, toinsert)
>>> l
[1, 2, 3, 3, 5, 10, 11]
>>> 
