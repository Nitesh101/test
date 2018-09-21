"""
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
	def __del__(self):
    		print "destructor"
		raise Exception("raise")
def main():
	a=input("Enter a value: ")
	b=input("Enter a b value: ")
	val = cal(a,b)
#	del.val()
	print val.add()
	print val.sub()
	print val.mul()
	print val.div()
if __name__ == "__main__":
	main()

class divisible:
	def __init__(self):	
		pass
	def putNumbers(self,num,limit):
    		i=0
		while i<=limit:
			if i%num == 0:
				yield i
			i+=1
obj = divisible()
num = input("Enter a number: ")
limit = input("Enter a range: ")
for index in obj.putNumbers(num,limit):
	print index
"""

