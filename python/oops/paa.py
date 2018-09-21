class BankAccount:
	def __init__(self):
		self.balance = 0
	def withdraw(self,amount):
		self.balance -=amount
		return self.balance
	def deposite(self,amount):	
		self.balance += amount
		return self.balance
	def current_balance(self,amount):
		self.balance = amount
		return self.balance
		 
a = BankAccount()
print a.deposite(100)
print a.withdraw(50)
print a.current_balance(10)
