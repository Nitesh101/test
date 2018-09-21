from operator import itemgetter
l = [(1,3,4),(3,2,5),(2,1,3),(7,7,2)]
x = sorted(l,key=itemgetter(2))
print x
