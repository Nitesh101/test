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
dqueue1 = Deque()
