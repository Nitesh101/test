#!/usr/bin/python
class Deque:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []	
	def addfront(self,item):
		self.items.insert(0,item)
		print(self.items)
	def addrear(self,item):
		self.items.append(item)
		print(self.items)
	def removefront(self):
		return self.items.pop(0)
		print(self.items)
	def removerear(self):
		return self.items.pop()
		print(self.items)
	def size(self):
		return len(self.items)
	def display(self):
		return self.items
		print(self.items)
d=Deque()
print "the dqueue is empty: ",(d.isEmpty())
d.addrear(4)
d.addfront('dog')
d.addrear('cat')
d.addrear('nitesh')
print "the size of dqueue is:",(d.size())
print "after delete rear is:", (d.removerear())
print "after delete front is:", (d.removefront())
print (d.display())
