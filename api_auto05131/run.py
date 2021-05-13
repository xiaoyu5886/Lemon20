# TIME: 2021/5/13 9:45
# author: xiaoyu

from common.fun_qcd import api_log,read_case,write_case
case_list = read_case("C:\\tool\python_workspacea\\api_auto05131\\test_data\\test_case_api.xlsx","register")
print(case_list)
print("--"*20)
for case in case_list:
    print(case)
    id = case["id"]
    url =case["url"]
    data =eval(case["data"])
    exceped =eval(case["exceped"])
    code =exceped["code"]
    msg =exceped["msg"]

    log_res = api_log(url=url,data=data)
    # print(log_res)
    final_code =log_res["code"]
    final_msg =log_res["msg"]

    if final_code==code and final_msg==msg:
        print("这{}条用例通过".format(id))
        final_write ="通过05131"
    else:
        print("这{}条用例通过".format(id))
        final_write = "通过05131"

    write_case("C:\\tool\python_workspacea\\api_auto05131\\test_data\\test_case_api.xlsx","register",row=id+1,column=8,final_write=final_write)
    print("****"*20)

from common.fun_qcd import api_log,read_case,write_case
case_list = read_case("C:\\tool\python_workspacea\\api_auto05131\\test_data\\test_case_api.xlsx","login")
print(case_list)
print("--"*20)
for case in case_list:
    print(case)
    id = case["id"]
    url =case["url"]
    data =eval(case["data"])
    exceped =eval(case["exceped"])
    code =exceped["code"]
    msg =exceped["msg"]

    log_res = api_log(url=url,data=data)
    # print(log_res)
    final_code =log_res["code"]
    final_msg =log_res["msg"]

    if final_code==code and final_msg==msg:
        print("这{}条用例通过".format(id))
        final_write ="通过05131"
    else:
        print("这{}条用例通过".format(id))
        final_write = "通过05131"

    write_case("C:\\tool\python_workspacea\\api_auto05131\\test_data\\test_case_api.xlsx","login",row=id+1,column=8,final_write=final_write)
    print("****"*20)