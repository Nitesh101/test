class Animal:
	def __init__(self,name):
		self.name = name
	def talk(self):
		raise NotImplementedError("subclass must implemeted absta")
class Cat(Animal):
	def talk(self):	
		return "meow"
class Dog(Animal):
	def talk(self):
		return "woof woof"
animals = [Cat('Missy'),Cat('Mr.misoffelees'),Dog('Lassie')]
for animal in animals:
	print animal.name + ':'+animal.talk()
