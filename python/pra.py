#!/usr/bin/python
class StackClass:

    def __init__(self, itemlist=[]):
        self.items = itemlist

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1:][0]
    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)
        return 0
stack = StackClass()
stack.peek()
stack.pop()
stack.push(10)
print stack
