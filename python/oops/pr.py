class animal:
	def eat(self):
		print "eating"
class dog(animal):
	def bark(self):
		print "barking"
class baby(dog):
	def sweep(self):
		print "sweeping"
c = baby()
c.sweep()
c.eat()
c.bark()
