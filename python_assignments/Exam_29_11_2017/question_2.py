from operator import itemgetter
val = (('tom',19,80),('john',20,90),('jony',17,91),('jony',17,93),('json',21,85))
val2 = sorted(val,key=itemgetter(0))
print val2
