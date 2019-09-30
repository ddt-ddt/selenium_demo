import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://activity.baozun.com")
driver.find_element_by_link_text("开始使用").click()
time.sleep(3)
driver.find_element_by_css_selector("[type='text']").send_keys("jm006868")
driver.find_element_by_css_selector("[type='password']").send_keys("baozun123456")
time.sleep(3)
driver.find_element_by_css_selector("[type='button']").click()
time.sleep(5)
element = driver.find_element_by_xpath("//a[contains(@href,'#/help')]")
element.click()
time.sleep(3)
# handles=driver.window_handles
# driver.switch_to.window(handles[-1])