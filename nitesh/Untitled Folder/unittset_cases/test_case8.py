import unittest
import os
print "Execute Test case_ID_159: IP--->Call Put with wrong input data
val3 = os.system("python test1.py put 1")
print val3

class Testcase(unittest.Testcase):
	def test_put(self):
		self.assertEqual(val3,0)
if __name__=='__main__':
	unittest.main()