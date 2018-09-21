class Employee:
	def __init__(self,name):
		self.name = name
	def sales(self):
		print "Employee name: ",self.name
		val = input("enter the no of sales in month: ")
		self.val = val
		print "sales: ",self.val
	def bonus(self):
		if self.val >= 5000:
			self.bonus = (20*self.val)/100
		elif self.val <= 4999 and self.val >= 3000:
			self.bonus = (10*self.val)/100
			print "bonus: ", self.bonus
		else:
			print "no bonus"
a = Employee("nitesh")
a.sales()
a.bonus()
