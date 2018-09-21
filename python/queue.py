#!/usr/bin/python
class Queue:
        def __init__(self):
                self.item = []
        def append(self,item):
                self.item.append(item)
                print self.item
        def remove(self):
                self.item.pop(0)
		print self.item
        def isEmpty(self):
                return (self.item == [])
        def topOfstack(self):
                return len(self.item)
        def __str(self):
                return str(self.item)
queue1 = Queue()
queue1.append(10)
queue1.append(20)
queue1.append(30)
queue1.append(40)
queue1.remove()
queue1.remove()
#print queue1.self

