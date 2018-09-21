#!/usr/bin/python
from array import array

sLen = input("Enter stack length: ")

while not isinstance(sLen, int):
	print("Enter Integer value.")
	sLen = input("Enter stack length: ")

class Stack():
	def __init__(self):
		self.sArray = array('i')

	
	
	def display(self):
		if len(self.sArray) != 0:
			print(list(self.sArray))
		else:
			print('Empty List')

ex = Queue()

print("1: Insert\n2: Display\n3: Delete\n4: Exit")
opt = input("Enter your option: ")

while opt != 4:

	if opt == 1:
		ex.insert()

	elif opt == 2:
		ex.display()

	elif opt == 3:
		if 	len(ex.sArray) == 0:
			print("sueue is Empty, Insert Values.")
		else:
			ex.remove()

	print("1: Insert\n2: Display\n3: Delete\n4: Exit")
	opt = input("Enter your option: ")
