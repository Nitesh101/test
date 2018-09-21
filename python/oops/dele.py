class point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name,
p1 = point()
p2 = p1
print id(p1)
del p1
del p2
print p2
