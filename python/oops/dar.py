from operator import itemgetter
lst =  [(1, 3, 4), (3, 2, 5), (2, 1, 3), (7, 7, 2)]
x = sorted(lst,key=itemgetter(1))
print x
