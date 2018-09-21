class Employee:
	def __init__(self,name):
		self.name = name
	def sales(self):
		print "Employee name: ",self.name
		val = input("Enter no of sales: ")
		self.val = val
		print "sales",self.val
	def bonus(self):
		if self.val >= 50000:
			self.bonus=(20*self.val)/100
			print "bonus",self.bonus
		elif self.val <= 49999 and self.val >= 30000:
			self.bonus = (10*self.val)/100
			print "bonus",self.bonus
		else:
			print "no bonus"
a = Employee('nitesh')
a.sales()
a.bonus()
