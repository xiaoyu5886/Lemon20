# TIME: 2021/4/22 11:41
# author: xiaoyu

from common.def_fun import read_data,write_result,api_ful

#接口测试实战
#调用读取用例函数，调用接口请求函数（登录、注册），调用写入结果的函数  ---封装成函数
def excute(filename,sheetname,):
    cases = read_data(filename,sheetname)
    for dict1 in cases:
        # print(dict1)
        # print(type(i))
        case_id =dict1['case_id']
        url = dict1['url']
        data = eval(dict1['data'])
        # print(type(data))
        # print(case_id,url,data,expected)

        res = api_ful(url=url,data =data)
        print(res)

        expected = eval(dict1['expected'])  #获取预期结果的code和msg
        code = expected['code']
        msg = expected['msg']
        print("预期结果code: {},msg :{}".format(code,msg))

        real_code = res['code']
        real_msg = res['msg']

        print("实际结果code: {},msg :{}".format(real_code,real_msg))

        if code == real_code and msg==real_msg:
            print('第{}用例测试通过'.format(case_id))
            finl_result = 'passed'
        else:
            print('第{}用例测试不通过'.format(case_id))
            finl_result = 'false'

        write_result(filename,sheetname,case_id+1,8,finl_result)

        print('-' * 100)

excute('C:\\Users\\16506\\.jenkins\\workspace\\Test0422\\test0422\\testdata\\test_case_api.xlsx','register')
