import unittest
import os
print "Call init after Observe"
var=os.system("python run.py discover 1 observe 1 init 1")  
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Hello"
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()
