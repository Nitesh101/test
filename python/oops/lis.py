"""
#UPDATEING LISTS
lis = [1,2,3,'nitesh',5,6,7,'veera']
lis[2] = 10
print lis
#DELETE LIST IN ELEMENT
lis = [1,2,3,4,5]
del lis[1]
print lis
#LENGTH OF LIST
lis = [1,3,4,5,6]
print len(lis)

l = [1,23,4]
print tuple(l)


lis = [1,2,3,4,5]
del lis[3]
print lis

lis = [1,2,3,4,5]
lis.remove(3)
print lis

#LIST.APPEND(OBJ)
lis = [1,2,3,4,5,6]
lis.append(10)
print lis
#LIST.COUNT(OBJ)
lis = [1,2,2,3,4,2,4,5]
lis.count(2)
print lis

#LIST.EXTEND(SEQ)
lis = [1,2,3,4,5,6]
lis2 = [7,8,9,10,11]
lis.extend(lis2)
print lis

#LIST.INDEX?(OBJ)
lis = [1,2,3,4,5]
lis.index(3)
print lis

#LIST.INSERT(INDEX,OBJ)
lis = [1,2,3,4,5]
lis.insert(2,222)
print lis

#LIST.POP(OBJ=LIST[-1])
lis = [1,2,3,4,5,6]
lis.pop()
print lis
lis.pop(1)
print lis

#LIST.REMOVE(OBJ)
lis = [1,2,3,4,5]
print "before reomve element ",lis
lis.remove(4)
print "reomove perticular element in a list 4",lis
#DELETE ELEMENT
lis = [1,2,3,4,5]
print "before delete elements",lis
del lis[2]
print "delete a element using indexing in  a list  2",lis

#LIST.REVSRE()
lis = [1,2,3,4,5]
lis.reverse()
print lis

#LIST.SORT()
lis = [2,6,1,3,7,8]
lis.sort()
print lis
"""

