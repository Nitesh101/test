import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="/home/madisnit/home/madisnit/Downloads/geckodriver")
#driver = webdriver.Firefox()
driver.get("http://www.python.org")
print driver.title
assert "Python" in driver.title
 
# submit query
elem = driver.find_element_by_name("q")
elem.send_keys("python")
elem = driver.find_element_by_name("submit")
elem.click()
#elem.send_keys(Keys.RETURN)
 
# get performance data
#performance = driver.execute_script("return window.performance")
#print performance
 
#driver.close()
