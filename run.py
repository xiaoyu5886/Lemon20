# TIME: 2021/4/21 22:59
# author: xiaoyu

from common import del_fun
from testdata import testdata
from selenium import webdriver

#初始化启动浏览器
driver = webdriver.Firefox() #初始化启动浏览器
driver.implicitly_wait(10)
driver.maximize_window() #窗口最大化

# 取出实参
url = testdata.url['url']
username = testdata.use_info['username']
password = testdata.use_info['password']
s_key = testdata.s_key['s_key']
print(url,username,password,s_key)


#调用查询函数
result_num = del_fun.search_key(url=url, username=username, password=password, s_key=s_key, driver=driver)

# 判断查询结果是否正确
if s_key in result_num:
    print(result_num)
    print('查询结果正确：{}'.format(result_num))
else:
    print('查询结果错误：{}'.format(result_num))
