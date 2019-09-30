import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from automation_framwork.framwork.logger import Logger

# create a logger instance
logger = Logger(logger="BasePage").getlog()

class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver

    def back(self):
        """
        浏览器后退按钮
        :param none:
        """
        self.driver.back()
        logger.info("Click back on current page.")

    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()
        logger.info("Click forward on current page.")

    """
    BrowserEngine中已经包含
    def open_url(self, url):
        self.driver.get(url)
    """

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()
        logger.info("Quit browser.")

    def take_screenshot(self):
        """
        截图并保存在根目录下的Screenshots文件夹下
        :param none:
        """
        file_path = os.path.dirname(os.getcwd()) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Take screenshot and save it to /screenshots folder.")
        except Exception as e:
            logger.error("Failed to take screenshot %s" % e)

    def find_element(self, selector):
        """
        根据 => 来切分字符串
        submit_button = "id => su"

        id => su
        name => aaa
        xpath => //input[@a = a]

        driver.find_element_by_id('su')
        driver.find_element_by_name('aaa')
        driver.find_element_by_xpath('//input[@a = a]')

        :param selector:
        :return: element
        """

        element = ""

        # 默认通过id查找元素
        if "=>" not in selector:
            return self.driver.find_element_by_id(selector)

        selector_by = selector.split("=>")[0]
        selector_value = selector.split("=>")[1]

        if selector_by == "id":
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Find the element \' %s \' successful, by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" %e)
                self.take_screenshot()
        elif selector_by == "name":
            # try ... except ...
            # logger
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "class_name":
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "link_text":
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def type(self, selector, text):
        element = self.find_element(selector)
        element.clear()
        try:
            element.send_keys(text)
            logger.info("Type \' %s \' in input box." % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s." % e)
            self.take_screenshot()

    def click(self, selector):
        element = self.find_element(selector)
        try:
            element.click()
            logger.info("The element \' %s \' was clicked." % element.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title