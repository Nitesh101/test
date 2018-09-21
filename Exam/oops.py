class Employee:	
	def __init__(self,name):
		self.name = name
	def Sales(self):
		print "Employee name : ",self.name
		val = input("enter the no of sales in month: ")
		self.val = val
		print "sales ",self.val
	def Bonus(self):
		if self.val >= 5000:
			self.bonus=(20*self.val)/100
			print  "bonus",self.bonus
		elif self.val<=4999 and self.val>=3000:
			self.bonus=(10*self.val)/100
			print "bonus",self.bonus
		else:
			print "no bonus "
a = Employee("nitesh")
b = Employee("jolly")
a.Sales()
a.Bonus()
b.Sales()
b.Bonus()
