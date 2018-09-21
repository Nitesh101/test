from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Firefox(executable_path="/home/madisnit/home/Nitesh_old_backup/madisnit/Desktop/Sele/geckodriver")
#driver = webdriver.Firefox(executable_path="/home/madisnit/Downloads/geckodriver")
       
	#driver.maximize_window()
driver.get("https://login.yahoo.com/?.src=ym&.lang=en-IN&.intl=in&authMechanism=primary&done=https%3A%2F%2Fmail.yahoo.com%2Fd&eid=100&as=1&login=niteshveera.madisetty%40votarytech.com&crumb=ypYO%2F%2FiW5PL")
#time.sleep(8)
elem = driver.find_element_by_id("login-username")
elem.send_keys("m.veeranitesh")
#time.sleep(3)
button = driver.find_element_by_id("login-signin")
button.click()
#time.sleep(3)
elem = driver.find_element_by_id("login-passwd")
elem.send_keys("Nitesh12#")
#time.sleep(3)
button = driver.find_element_by_class_name("uh-menu uh-mail D(ib) Mstart(14px) ua-ie8_Pb(10px) ua-ie9_Pb(10px)").click()
button = driver.find_element_by_id("login-signin").click()
time.sleep(1)
driver.find_element_by_id("Compose").click()
time.sleep(2)
driver.find_element_by_id("to-field").send_keys("jvinaykumar055@yahoo.com")
time.sleep(2)
driver.find_element_by_id("subject-field").send_keys("code")
time.sleep(2)
text = driver.find_element_by_id("rtetext")
text.send_keys("prasad is good boy")
time.sleep(3)
attach_id = driver.find_element_by_id("attachment-button-input")
attach_id.click()
time.sleep(3)
'''
	attach_id.send_keys(os.getcwd()+"/a.txt")
        time.sleep(10)
	text.send_keys(Keys.CONTROL + Keys.ENTER)
        time.sleep(5)
	ActionChains(driver).move_to_element(driver.find_element_by_id("yui_3_10_3_1_1375219693637_127")).perform()
	driver.find_element_by_id("yucs-signout").click()
'''
driver.close()
#except Exception, e:
#	print str(e)
#	driver.close()
