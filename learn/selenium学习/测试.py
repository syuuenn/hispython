# encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(1)
# ret = driver.find_element_by_xpath('//a[@name="tj_trtieba"]').text
# driver.find_element_by_xpath('//a[@name="tj_trtieba"]').click()
driver.find_element_by_id('kw').send_keys('煎蛋')
driver.find_element_by_id('su').click()

print(driver.page_source.encode())
time.sleep(1)
driver.find_element_by_xpath('//*[@id=1]/h3/a[1]').click()
# driver.save_screenshot('a.png')
for i in driver.window_handles:
    print(i)
    driver.switch_to_window(i)

# print(ret)
#关闭浏览器
# driver.quit()
