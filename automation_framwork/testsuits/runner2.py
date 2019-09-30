# coding=utf-8
import unittest
from automation_framwork.testsuits.test_baidu_search import BaiduSearch

suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
# 虽然比addTest()方法有了一定的效率提升，但是也有一定局限性

if __name__ == '__main__':

    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)

