# coding=utf-8
import time
from selenium import webdriver
from framwork_demo.test1.basepage import BasePage
from framwork_demo.test1.browser_engine import BrowserEngine


class TestCase1(object):
    driver = webdriver.Chrome()

    # browserEngine = BrowserEngine(object)
    # driver = browserEngine.get_browser()

    driver.maximize_window()
    driver.implicitly_wait(10)

    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys("Selenium")
        time.sleep(1)
        self.basepage.back()
        self.basepage.forward()
        self.basepage.quit_browser()


baidu = TestCase1()
baidu.open_baidu()
baidu.test_search()