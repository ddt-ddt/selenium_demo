# coding=utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
import xmlrunner

test_dir = os.path.dirname(os.path.abspath('.'))+ '/testsuits'
suite = unittest.TestLoader().discover(test_dir, pattern='test*.py')

if __name__ == '__main__':

    # 执行用例
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(suite)
