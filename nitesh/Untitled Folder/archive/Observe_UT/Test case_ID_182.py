import unittest
import os
print "Call Observe with wrong input data with non secure connection"
var=os.system("python run.py init 1 discover 1 observe ")  
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Hello"
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()