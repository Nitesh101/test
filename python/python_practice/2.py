class Node:
	def __init__(self):
		self.item = None
		self.link = None
class Queue:
	def __init__(self):
		self.top = 0
		self.head = Node()
	def isEmpty(self):	
		return self.top == 0
	def insert(self):
		if len(self.slist)+1 > slen:
			print "stack is full"
		else:		
			value = input("enter a integer: ")
			count = 1
		while count == 1:
			try:
				self.slist.append(value)
				count =2
			except TypeError:
				print ("enter a integer value only: ")
	def remove(self):
		self.item.pop(0)
	def isEmpty(self):
		return (self.item == [])
	def topofstack(self.item):
		return len(slef.item)
		def __str__(self):
			str(self.item)
		def display(self):
			temp = self.head
			while temp.item:
				print temp.link
		print "\n"
