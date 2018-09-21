import unittest
import os
print "call get once"
var=os.system("python run.py discover 1 get 1") ## call get once
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Hello"
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()
