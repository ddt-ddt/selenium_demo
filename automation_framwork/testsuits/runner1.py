# coding=utf-8
import unittest

from automation_framwork.testsuits.test_baidu_search import BaiduSearch
from automation_framwork.testsuits.test_get_page_title import GetPageTitle

suite = unittest.TestSuite()
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(BaiduSearch('test_search2'))
suite.addTest(GetPageTitle('test_get_title'))
# 有局限性，如果有几百个测试类，需要这样手动去添加

if __name__ == '__main__':

    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)