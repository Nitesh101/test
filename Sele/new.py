from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(export="/home/madisnit/home/madisnit/Downloads/geckodriver")
#driver = webdriver.Firefox()
driver.get("http://www.google.com")
driver.get("https://in.yahoo.com")
driver.get("https://login.yahoo.com/?.src=fpctx&.intl=in&.lang=en-IN&authMechanism=primary&yid=&done=https%3A%2F%2Fin.yahoo.com%2F&eid=100&add=1")
driver.find_element_by_id("login-username").send_keys("m.veeranitesh")
#driver.find_element_by_id("login-signin").click()
driver.find_element_by_id("login-sigin").send_keys();
send_keys(keys.RETURN)
#driver.get("https://login.yahoo.com/account/create?authMechanism=primary&yid=&done=https%3A%2F%2Fin.yahoo.com%2F&eid=100&add=1&src=fpctx&intl=in&lang=en-IN&specId=yidReg")

