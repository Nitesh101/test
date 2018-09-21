#!/usr/bin/python
from selenium import webdriver
d = webdriver.Firefox(executable_path="/path/to/geckodriver")
d.get("http://www.google.com")
