import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
element = browser.find_element_by_link_text("登录")
element.click()
time.sleep(3)
element1 = browser.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')
element1.click()
time.sleep(8)
submit_element = browser.find_element_by_xpath("//input[@type='submit']")
submit_element.submit()
