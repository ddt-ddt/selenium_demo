import time


class TestGetTime(object):

    def get_system_time(self):
        print(time.localtime())
        new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 格式化时间，按照 YYYY-mm-dd HH:MM:SS 的格式打印出来
        print(new_time)


gettime = TestGetTime()
gettime.get_system_time()