import unittest
import os
print "Call Get once to non secure connection"
var=os.system("python run.py init 1 discover 1 observe 1") ## Call Get once to non secure connection 
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Hello"
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()
