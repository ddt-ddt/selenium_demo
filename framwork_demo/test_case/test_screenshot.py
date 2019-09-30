# coding=utf-8
import time
from selenium import webdriver

from framwork_demo.test1.basepage import BasePage


class TestScreenshot(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    basepage = BasePage(driver)

    def test_take_screen(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)
        self.basepage.take_screenshot()
        self.basepage.quit_browser()


test = TestScreenshot()
test.test_take_screen()