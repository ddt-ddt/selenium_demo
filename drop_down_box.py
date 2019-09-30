from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

element = driver.find_element_by_id("searchDropdownBox")
select = Select(element)
# select.select_by_value("search-alias=toys-and-games")

#select.select_by_index(0)

select.select_by_visible_text("Toys & Games")
