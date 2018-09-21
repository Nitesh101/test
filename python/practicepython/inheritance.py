class vahicle:
	def __init__(self,name,color):
		self.name = name
		self.color = color
	def get_details(self):
		return self.name + " " +self.color
class car(vahicle):
	def __init__(self,wheels,body):
		self.wheels = wheels
		self.body = body
	def get_car(self):	
		return self.wheels + " " +self.body
g = vahicle("mustong","red")
h = car(4,"metal")
print h.get_car()
print g.get_details()
