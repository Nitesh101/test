#/usr/bin/python
class divisible:
	def __init__(self):	
		pass
	def putNumbers(self,num,limit):
    		i=1
		while i<limit:
			if i%num == 0:
				yield i
			i+=1
obj = divisible()
num = input("Enter a number: ")
limit = input("Enter a range: ")
for index in obj.putNumbers(num,limit):
	print index
if __name__ == "__main__":
	divisible()
