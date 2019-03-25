import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
element = driver.find_element_by_link_text("登录")
element.click()
time.sleep(3)
element1 = driver.find_element_by_xpath("//p[text()='用户名登录']").click()
time.sleep(3)
checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")
checkbox.click()
print(checkbox.is_selected())
