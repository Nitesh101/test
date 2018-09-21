""""
#class Person:
#	def __init__(self,name,salary):
#		self.name = name
#		self.salary = salary
#	def getName(self):
#		return self.name
#	def getSalary(self):
#		return self.salary
#	def isEmployee(self):		
#		return False
#class Employee(Person):
#	def isEmployee(self):
#		return True
#emp = Person("Geek1",4000)
#print emp.getName()
#print emp.getSalary()
#emp = Employee("Geek2",5000)
#print emp.getName(), emp.getSalary()
"""
"""
class Dog:
	def __init__(self,name):
		self.name = name
		self.trick = []
	def getName(self):
		return self.name
	def add_trick(self,trick):
		self.trick.append(trick)
d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")
print d.trick
print d.getName()
print e.getName()
"""
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
e = Bag()
e.add(4)
print e.add(5)
