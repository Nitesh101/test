import unittest
import os
print "Test case_ID_135--->Call Get from multiple clients"
var=os.system("python run.py discover 1 get 3") 
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Hello"
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()
