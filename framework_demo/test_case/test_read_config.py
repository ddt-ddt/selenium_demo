# coding=utf-8
from backports import configparser
import os


class TestReadConfigFile(object):

    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))  # 获取项目根目录的相对路径
        print(root_dir)

        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")

        return (browser, url)  # 返回的是一个元组


trcf = TestReadConfigFile()
print(trcf.get_value())