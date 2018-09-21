class vector():
	def __init__(self,num1,num2):
		self.num1=num1
		self.num2=num2
	def __add__(self,other):
		return (self.num1+other.num1,self.num2+other.num2)
	def __sub__(self,other):
		return (self.num1-other.num1,self.num2-other.num2)
	def __mul__(self,other):
		return (self.num1*other.num1,self.num2*other.num2)
	def __repr__(self):
		return (self.num1,self.num2)
	def __del__(self):
		print "destroying"
		return

def main():
	vect1=vector(2,3)
	vect2=vector(2,3)
	print vect1+vect2
	print vect1-vect2
	print vect1*vect2
	del vect1

if __name__=="__main__":
	main()


