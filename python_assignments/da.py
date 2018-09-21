from operator import itemgetter
d = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
val = sorted(d,key=itemgetter(1))
print val
