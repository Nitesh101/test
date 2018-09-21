"""
class Vehicle:
	def __init__(self,name,color):
		self.name = name
		self.color = color
	def getcolor(self):
		return self.color
	def setcolor(self):	
		self.color = color
	def getname(self):
		return self.name
class Car(Vehicle):
	def __init__(self,name,color,model):
		super().__init__(name,color)
		self.__model = model
	def getDescription(self):
		return self.getname()+self.model+"in"+self.getcolor()+" color"
c = Car("Ford Musting","red","GT350")
print c.getDescription()
"""

class (object):
	pass
