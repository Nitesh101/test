#!/usr/bin/python
slen = input("enter stack length: ")
while not isinstance(slen,int):
	print ("enter a integer value")
	slen = input("enter stack length: ")
class Stack():
	def __init__(self):
		self.slist = list
	def insert(self):
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
		self.slist.pop()
	def display(self):
		if len(self.slist)!=0:
			print(list(self.slist))
		else:
			print("Empty list")
ex = Stack()

print("1: Insert\n2: Display\n3: Delete\n4: Exit")
opt = input("Enter your option: ")

while opt != 4:

        if opt == 1:
                ex.insert()

        elif opt == 2:
                ex.display()

        elif opt == 3:
                if      len(ex.slist) == 0:
                        print("Stack is Empty, Insert Values.")
                else:
                        remove()

        print("1: Insert\n2: Display\n3: Exit\n")
        opt = input("Enter your option: ")

