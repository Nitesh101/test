#/usr/bin/python
class Stack():
        def __init__(self):
                self.item = []
        def push(self,item):
                self.item.append(item)
                print self.item
        def pop(self):
                return self.item.pop()	
		print self.item
        def isEmpty(self):
                return (self.item == [])
        def topOfStack(self):
                return len(self.item)
        def __str__(self):
                return str(self.item)
stack1=Stack()

