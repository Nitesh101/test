import unittest
import os
print "Test case_ID_168--->Call Get with wrong input data"
var=os.system("python run.py discover 1 get ") 
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Hello"
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()
