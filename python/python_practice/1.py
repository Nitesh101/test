#!/usr/bin/python
class Node:
	def __init__(self):
		self.item = None
		self.link = None
class Stack:
	def __init__(self):
		self.top = 0
		self.head = Node()
	def isEmpty(self):
		return self.top == 0
	def push(self.item):
		oldHead = self.head
		self.head = Node()
		self.head.item  = item
		self.head.link = oldhead
		self.top += 1
	def pop(self):
		item = self.head.item
		self.head = self.head.link
		self.top -=1
		return item
	def display(self):
		temp = self.head
		while temp.item:
			print temp.item,
		print "\n"
s = Stack()
s.push(20)
s.push(10)
s.display()
s.pop()
s.display()
print("1: Insert\n2: Display\n 3 : Delete\n4 : Exit")
opt = input("Enter  a your options: ")
while opt != 4:
	if opt ==1:
		data = input("enter value")
		s.push(data)
	elif opt == 2:	
		s.display()
	elif opt == 3:
		if s.isEmpty():
			print "stack is Empty"
		else:
			s.pop()
	print("1 : Insert\n2: Display\n3: Delete\n4: Exit")
	opt = input("Enter a your option: ")
