from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/')

actions = ActionChains(driver)
element = driver.find_element_by_id('nav-link-accountList')
actions.move_to_element(element).perform()
driver.find_element_by_xpath('//span[text()="Sign in"]').click()

# driver.quit()