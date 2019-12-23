import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from selenium import webdriver
import os.path
import configparser
from framwork.logger import Logger

logger = Logger(logger = "BrowserEngine").getlog()

class BrowserEngine(object):
    """
    定义一个浏览器引擎类，根据browser_type的值去，控制启动不同的浏览器，这里主要是IE，Firefox, Chrome
    """

    def __init__(self, driver):
        self.driver = driver

    def get_browser(self,driver):
        """
        从配置文件读取启动哪种浏览器
        :return: driver
        """
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        file_path = rootPath + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You select %s browser." %browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" %url)

        if browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == 'Chrome':
            driver = webdriver.Chrome()
            logger.info("Starting chrome browser.")
        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info("Starting IE browser.")
        else:
            driver = webdriver.Chrome()
            logger.info("Starting chrome browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10s.")

        return driver

    def quit_browser(self):
        logger.info("Close and quit the browser.")
        self.driver.quit()