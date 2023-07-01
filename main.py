import time

import selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("https://thoothukudi.nic.in/about-district/list-of-collectors/")
time.sleep(20)