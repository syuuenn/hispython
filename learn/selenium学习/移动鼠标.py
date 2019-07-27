# encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(1)
ret = driver.find_element_by_xpath('//a[@name="tj_trtieba"]')
ret1 = driver.find_element_by_xpath('//a[@name="tj_trtieba"]')
ret2 = driver.find_element_by_xpath('//a[@name="tj_trtieba"]')
ActionChains(driver).move_to_element(ret).perform()#移动到
ActionChains(driver).move_to_element(ret).click(ret).perform()#单击
ActionChains(driver).move_to_element(ret).double_click(ret).perform()#双击
ActionChains(driver).move_to_element(ret).context_click(ret).perform()#右击
ActionChains(driver).move_to_element(ret).click_and_hold(ret).perform()#长按
ActionChains(driver).move_to_element(ret).drag_and_drop(ret1,ret2).perform()#将元素1移动到元素2