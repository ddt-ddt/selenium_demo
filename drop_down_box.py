from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

select = Select(driver.find_element_by_id("searchDropdownBox"))
# select.select_by_value("search-alias=toys-and-games")
#
# select.select_by_index(2)

select.select_by_visible_text("Toys & Games")
