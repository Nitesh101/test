import unittest
import os
print "BLE --> Call init after discover "

var=os.system("python run.py discover 1 init 1")
print var
class init(unittest.TestCase):
	def test_init(self):
		print "Entering into the unit test case "
		self.assertEqual(var,0)
if __name__=='__main__':
	unittest.main()
