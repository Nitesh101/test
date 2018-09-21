import unittest
import os
print ("Execute Test case_ID_213---->Call init after Put")
#val = os.system("python run.py init 1 ")
#val2 = os.system("python run.py discover  1 ")
val3 = os.system("python run.py init 1 discover 1 put 1 ")
print val3
class TestCase(unittest.TestCase):
	def test_put(self):
		self.assertEqual(val3,0)
	#	self.assertEqual(val2,0)
	#	self.assertEqual(val3,0)
if __name__=='__main__':
	unittest.main()
