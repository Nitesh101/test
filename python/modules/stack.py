#!/usr/bin/python
class Stack:
	def __init__(self):
		self.item = []
	def push(self,item):
		self.item.append(item)
	def pop(self):	
		return self.item.pop()
	def isEmpty(self):
		return (self.item == [])
	def topofStack(self):
		return len(self.item)
	def __str__(self):
		return str(self.item)	
stack1=Stack()
"""
if __name__ == "__main__":
	stack = Stack()
	stack.push(20)
	stack.push(30)
	stack.push(70)
	stack.push(80)
	print stack
	stack.pop()
	print stack
	print stack.topofStack()
"""
