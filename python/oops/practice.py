class User:
	def __init__(self,name):
		self.name = name
	def printName(self):
		print "Name =" + self.name
class Programmer(User):
	def __init__(self,name):
		self.name = name
	def dopython(self):
		print "programing python"
a = User("nitesh")
a.printName()
b = Programmer("shravani")
b.printName()
b.dopython()
