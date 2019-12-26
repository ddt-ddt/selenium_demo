# coding=utf-8
import os
import time
import unittest
from tools.HTMLTestRunner import HTMLTestRunner

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
file_open = open(HtmlFile, "wb")


test_dir = os.path.dirname(os.path.abspath('.'))+ '/testsuits'
suite = unittest.TestLoader().discover(test_dir, pattern='test*.py')

if __name__ == '__main__':

    # 执行用例
    runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=file_open, title=u"xx项目测试报告", description=u"用例测试情况")
    runner.run(suite)
    file_open.close()