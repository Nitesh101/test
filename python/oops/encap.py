class banckAccount:
	def __init__(self,name,accountNumber,balance):
		self.name = name
		self.number = accountNumber
		self.balance = balance
	def getBalance(self):
		return self.balance
myaccount = banckAccount("Nitesh",1101,1000)
print myaccount.name
print myaccount.number
print myaccount.getBalance()
