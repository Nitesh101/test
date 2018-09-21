#!/usr/bin/python
class Queue:
        def __init__(self):
                self.item = []
        def append(self,item):
                self.item.append(item)
                print self.item
        def remove(self):
                self.item.pop(0)
        def isEmpty(self):
                return (self.item == [])
        def topOfstack(self):
                return len(self.item)
        def __str(self):
                return str(self.item)
queue1 = Queue()

