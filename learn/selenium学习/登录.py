# encoding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
#登录git
driver.get("https://github.com/login")
time.sleep(1)
time.sleep(0.5)
driver.find_element_by_id('login_field').send_keys('syuuenn')
time.sleep(0.5)
driver.find_element_by_id('password').send_keys('jjk1254107619')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[4]').click()
time.sleep(0.5)
print(driver.get_cookies())

#登录哔哩哔哩
