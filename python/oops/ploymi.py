class dog(object):
	def sound(self):
		print "grorr"
class bear(object):
	def sound(self):	
		print "woof woof"
def makesound(animal):
	animal.sound()
Bear = bear()
Dog = dog()
makesound(Bear)
makesound(Dog)
