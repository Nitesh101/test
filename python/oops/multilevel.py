"""
#multilevel ineritance
class Animal:
	def eat(self):
		print "Eatting"
class Dog(Animal):
	def bark(self):
		print "Barking"
class BabyDog(Dog):
	def weep(self):
		print "weeping"
d = BabyDog()
d.eat()
d.bark()
d.weep()
"""
class Votary:
	def python(self):
		print ("python employees")
class Testing(Votary):	
	def Automation(self):
		print ("Automation testing")
class Manual(Testing):
	def scripts(self):
		print ("Manual scripts")
d = Manual()
d.python()
d.Automation()
d.scripts()

