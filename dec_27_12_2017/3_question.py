#!/usr/bin/python
def movenumber(mylist):
		op=[]
		index=0
		for val in mylist:
			if val > 0:
				op.insert(index,val)
				index+=1
			else:
				op.append(val)
		return op
print movenumber([1,-1,3,2,-7,-5,11,6])
print movenumber([-5,7,-3,-4,9,10,-1,11])
