# coding=utf-8
import os
import unittest

test_dir = os.path.dirname(os.path.abspath('.'))+ '/testsuits'
suite = unittest.TestLoader().discover(test_dir, pattern='test*.py')

if __name__ == '__main__':

    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
