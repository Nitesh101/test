from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="/home/madisnit/home/madisnit/Downloads/geckodriver")
driver.get("http://www.google.com")
driver.get("https://in.yahoo.com/")
driver.get("https://login.yahoo.com/config/login?.src=fpctx&.intl=in&.lang=en-IN&.done=https%3A%2F%2Fin.yahoo.com")
driver.find_element_by_id("login-username").send_keys("m.veeranitesh")
driver.find_element_by_name("signin").click()
driver.find_element_by_id("login-passwd").send_keys("Nitesh12#")
driver.find_element_by_name("verifyPassword").click()
driver.find_element_by_id("uh-mail-link").click()
send_keys(keys.RETURN)
