import unittest
import os
print "ALL resources --> Call Discover from multiple clients "

var=os.system("python run.py init 1 discover 2")
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Entering into the unit test case "
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()
