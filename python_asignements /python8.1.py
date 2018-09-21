class Vector:
	def __init__(self,num1,num2):
		self.num1 = num2
		self.num2 = num2
	def __add__(self,other):
		return self.num1+other.num1,self.num2+other.num2
	def __sub__(self,other):
		return self.num1-other.num1,self.num2-other.num2
	def __mul__(self,other):
		return self.num1-other.num1,self.num2-other.num2
	def __div__(self,other):
		return self.num1-other.num1,self.num2-other.num2
	def __repr__(self):
		 return self.num1,self.num2
	def __del__(self):
		print "destoring"
		return
def main():
	vect1 = Vector(3,5)
	vect2 = Vector(5,6)
	print vect1+vect2
	print vect1-vect2
	print vect1/vect2
	#del vect1
if __name__ == "__main__":
	main()
