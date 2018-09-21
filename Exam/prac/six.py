class inputoutput(object):
	def __init__(self):
		self.s = " "
	def getstring(self):
		self.s =raw_input()
	def printstring(self):
		print self.s.upper()
strobj = inputoutput()
strobj.getstring()
strobj.printstring()
