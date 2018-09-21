import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="/home/madisnit/home/Nitesh_old_backup/madisnit/Desktop/Sele/geckodriver")
driver.get("http://www.mail.yahoo.com")

print driver.current_url

logintxt = driver.find_element_by_name("username")
logintxt.send_keys("niteshveera.madisetty@votarytech.com")
button = driver.find_element_by_id("login-signin")
button.click()
pwdtxt = driver.find_element_by_id("login-passwd")
time.sleep(1)
pwdtxt.send_keys("Nitesh12#")
button = driver.find_element_by_name("verifyPassword")
button.click()
#button = driver.find_element_by_name("skip")
#button.click()
button = driver.find_element_by_class_name("frost-btn frost").click()
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
#button = driver.find_element_by_id("D(ib) Fz(14px) Fw(b) Va(t) C(#4d00ae) Lh(37px)")
#button.click()
#button = driver.find_element_by_class_name("uh-mail-icon Lh($userNavIconLh) W(28px) C(#6001d2) Mend(10px) Fz(30px) Grid-U Icon-Fp2 IconMail")
#button.click()
#selenium.find_element_by_name("verifyPassword").click()class=" D(ib) Fz(14px) Fw(b) Va(t) C(#4d00ae) Lh(37px)"
print driver.current_url

