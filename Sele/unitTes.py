import unittest
from selenium import webdriver

class TestGmail(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def testLogin(self):
		driver = self.driver
		driver.get('https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier')
		self.assertIn('Gmail', driver.title)
		loginBox = driver.find_element_by_id('Email')
		loginBox.send_keys('m.veeranitesh@gmail.com')
		pwBox = driver.find_element_by_id('Passwd')
		pwBox.send_keys('Nitesh12#')
		signinBtn = driver.find_element_by_id('signIn')
		signinBtn.click()

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2)
