import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox(executable_path="/home/madisnit/home/madisnit/Downloads/geckodriver")
driver = webdriver.Firefox()
driver.get("https://login.yahoo.com")

print driver.current_url

logintxt = driver.find_element_by_name("username")
logintxt.send_keys("m.veeranitesh")
button = driver.find_element_by_id("login-signin")
button.click()
pwdtxt = driver.find_element_by_name("password")
pwdtxt.send_keys("Nitesh12#")
#button = driver.find_element_by_name("verifyPassword")
submitBtn=browser.find_element_by_id("verifyPassword")
submitBtn.click()
