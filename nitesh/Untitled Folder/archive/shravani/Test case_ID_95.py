import unittest
import os
print "Test case_ID_95--->Call Get repeatedly for different resource"
var=os.system("python run.py discover 1 get 1") 
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Hello"
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()
