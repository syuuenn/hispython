# encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

js = 'alert("ok")'
driver.execute_script(js)

print(driver.switch_to_alert)