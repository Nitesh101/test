class bankAccount:
	def __init__(self,name,accountnumber,balance):
		self.name = name
		self.number = accountnumber
		self.__balance = balance
	def getBalance(self):
		return self.__balance
myaccount = bankAccount("nitesh",101,1000)
mydata = bankAccount("uday",102,10000)
print mydata.name
print mydata.number
print mydata.getBalance()
print myaccount.name
print myaccount.number
print myaccount.getBalance()
