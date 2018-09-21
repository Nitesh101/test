class inputoutput(object):
	def __init__(self):
		self.s = " "
	def getstring(self):
		self.s=raw_input("Enter a string: ")
	def printstring(self):
		print self.s.upper()
obj=inputoutput()
obj.getstring()
obj.printstring()
