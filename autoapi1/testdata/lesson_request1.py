# TIME: 2021/4/18 19:45
# author: xiaoyu

# 注册接口
'''

import requests #导入第三方库， 目前还没有使用是灰色的
url_reg = 'http://8.129.91.152:8766/futureloan/member/register'    #请求地址
data_reg = {"mobile_phone": '18720031763', "pwd": "lemon666", "type": "1", "reg_name": "lemon"}   #请求参数
header_reg = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json'}  #请求头

res = requests.post(url=url_reg, json = data_reg, headers=header_reg) #调用post函数，返回值接收，
# 这里接收的是http状态码
# print(res)   #返回的是http状态码
# print(res.status_code)   #返回的code码
print(res.headers)       #返回的响应头部
print(res.text)          #返回的响应正文，如果接口文档没有写明是json格式就用.text, 获取的是文本信息，是字符串
print(res.json())        #返回的响应正文，接口文档写明是json格式就用json（字典）, 方便后面需要做取值
# print(res.content)      #了解，返回的响应正文，是二进制，没有解密的

'''

import  requests
# 登录接口
url_login = 'http://8.129.91.152:8766/futureloan/member/login'
data_login = {"mobile_phone": "18720031763", "pwd": "lemon666"}
header_login = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json'}

login_result = requests.post(url= url_login, json= data_login, headers = header_login)
# print(login_result.headers)
print(login_result.json())

# 充值接口
# 如何获取token方式一
# id = login_result.json()['data']['id']   #获取id
# token = login_result.json()['data']['token_info']['token']   #获取token

# 如何获取token方式二 jsonpath
import  jsonpath   #导入jsonpath库
token = jsonpath.jsonpath(login_result.json(), '$.data.token_info.token')[0]  #从登录接口返回的正文里面取token, 调用jsonpath库的函数，用以前学的json取值的方法
id = jsonpath.jsonpath(login_result.json(), '$..id')[0]  #从登录接口返回的正文里面取id, 调用jsonpath库的函数,用以前学的json取值的方法
# print(id)   #返回的是list列表,如果要取值要用id[0]
# print(token)  #返回的是list列表，如果要取值要用token[0]

# 调用函数

url_recharge = 'http://8.129.91.152:8766/futureloan/member/recharge'
data_recharge = {"member_id": id,"amount": "500000"}
header_recharge = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json','Authorization': 'Bearer'+' '+token}

recharge_result = requests.post(url= url_recharge, json= data_recharge, headers = header_recharge)
# print(recharge_result.headers)
print(recharge_result.json())




