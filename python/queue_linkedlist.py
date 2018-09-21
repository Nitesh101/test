#!/usr/bin/python
class Node:
	def __init__(self):
		self.item = None
		self.link = None
class Queue:
	def __init__(self):
		self.top  = 0
		self.head = Node()
	def isEmpty(self):
		return self.top == 0
	def insert(self,value):
		if len(self.slist)+1 >slen:
			print "stack is full"
		else:
			value = input("enter an integer: ")
			count = 1
		while count == 1:
			try: 
				self.slist.append(value)
				count = 2
			except TypeError:
				print("enter a integer valuei only: ")
				value = input("enter an integer value: ")
			
    	def remove(self):
    		self.item.pop(0)
			#	print self.item
    	def isEmpty(self):
    		return (self.item == [])
    	def topOfstack(self):
			return len(self.item)
   			def __str__(self):
				return str(self.item)
			def display(self):
				temp = self.head
				while temp.item:
					print temp.item,
					temp = temp.link
			print "\n"
queue1 = Queue()
queue1.insert(0,10)
queue1.append(20)
queue1.append(30)
queue1.append(40)
queue1.remove()
queue1.remove()
print ("1 : Insert\n2: Display\n3 : Delete\n4 Exit")
opt = input("Enter a your option: ")
while opt != 4:
	if opt == 1:
		data = input("Enter Value: ")
		s.append(data)
	elif opt == 2:
		s.display()
	elif opt == 3:
		if 	s.isEmpty():
			print "stack is Empty"
		else:
			s.pop(0)
	
	print ("1 : Insert\n2: Display\n3 : Delete\n4 Exit")
	opt = input("Enter a your option: ")
