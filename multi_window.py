import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
time.sleep(1)

driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a").click()
print(driver.current_window_handle)  # 输出当前窗口句柄
handles = driver.window_handles  # 获取当前全部窗口句柄集合
print(handles)  # 输出句柄集合

# handles[0]代表最初打开的窗口
# handles[-1]代表最新打开的窗口

driver.switch_to.window(handles[0])
driver.find_element_by_link_text("努力创造光耀时代 光耀世界的中华文化").click()
time.sleep(5)
driver.switch_to.window(handles[1])
time.sleep(5)

# for handle in handles:  # 切换窗口
#     if handle == driver.current_window_handle:
#         print('switch to second window', handle)
#         time.sleep(5)
#         # driver.close()  # 关闭第一个窗口
#         driver.switch_to.window(handle)  # 切换到第一个窗口
#         time.sleep(5)

driver.quit()