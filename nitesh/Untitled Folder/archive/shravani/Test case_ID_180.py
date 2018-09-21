import unittest
import os
print "Test case_ID_180--->Call Get with wrong input data with non secure connection"
var=os.system("python run.py discover 1 get ") 
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Hello"
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()
