# coding=utf-8
import time
from selenium import webdriver
from framwork_demo.test1.logger import Logger

mylogger = Logger(logger='TestLog').getlog()


class TestLog(object):

    def print_log(self):
        driver = webdriver.Chrome()
        mylogger.info("打开浏览器")
        mylogger.debug("debug")
        driver.maximize_window()
        mylogger.info("最大化浏览器窗口。")
        driver.implicitly_wait(8)

        driver.get("https://www.baidu.com")
        mylogger.info("打开百度首页。")
        time.sleep(1)
        mylogger.info("暂停一秒。")
        driver.quit()
        mylogger.info("关闭并退出浏览器。")


testlog = TestLog()
testlog.print_log()