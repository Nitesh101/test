import unittest
import os
print ("Execute Test Case_ID_69:---> Call Put repeatedly  to secured connection by Authorized client for same resource.")
val = os.system("python run.py init 1 discover 1 get 1 put 1")
print val
class TestCase(unittest.TestCase):
	def test_put(self):
		self.assertEqual(val,0)

if __name__=='__main__':
	unittest.main()
