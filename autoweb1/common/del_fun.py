# TIME: 2021/4/21 22:57
# author: xiaoyu


# web自动化基础
# 导入库和源
from selenium import webdriver
import time

#封装函数-打开网页
def open_url(url,driver):
    driver.get(url)  #打开指定地址
    driver.maximize_window() #窗口最大话

# 封装函数-登录
def login(username,password,driver):
    driver.find_element_by_id('username').send_keys(username)  #输入用户名
    driver.find_element_by_id('password').send_keys(password)     #输入密码
    driver.find_element_by_id('btnSubmit').click()            #点击登录

# 封装函数：查询订单号
def search_key(url,username,password,s_key,driver):
    open_url(url,driver)
    login(username,password,driver)
    time.sleep(2)

    # 打开零售出库页面
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(2)

    # 切换到iframe，输入查询内容
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/pages/materials/retail_out_list.html"]'))
    time.sleep(2)
    driver.find_element_by_id('searchNumber').send_keys(s_key)
    time.sleep(2)

    #点击搜索
    driver.find_element_by_xpath('//a[@id="searchBtn"]').click()
    time.sleep(2)

    #从查询结果页找到这个订单号码
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div[@class="datagrid-cell datagrid-cell-c1-number"]').text
    return num


