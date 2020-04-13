import datetime
import requests
import pandas as pd


def getstationaddress(cookie,statusdict,buinessdict,registStatusedic):

    """获取站址信息"""

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',

        'Connection': 'keep-alive',
        'Content-Length': '61',
        'Cookie': cookie,
        'Host': '180.153.49.85:58580',
        'Origin': 'http://180.153.49.85:58580/basisrs/activeAlarm/allActiveAlarmList.jsp',
        'Pragma': 'no-cache',
        'Referer': 'http://www.chinaooc.cn/front/show_index.htm',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    form_data = {
        "businesstype":'2',
        "page":"1",
        "rows":'1'}
    url = 'http://180.153.49.85:58580/station?datagrid'    # 请求地址
    response = requests.post(url, data=form_data, headers=headers)  # 发起请求
    print(response.json())
    print(response.json().get("total"))   # 获取返回数据条数
    rows = str(response.json().get("total"))
    #rows = 100
    '''===========第二次获取全部数据=========='''
    form_data = {
        "page": "1",
        "rows": rows
    }

    response = requests.post(url, data=form_data, headers=headers)   # 发起请求
    print(response.json().get("total"))
    rowslist1 = response.json().get("rows")   # 获取返回数据
    data = pd.DataFrame(rowslist1)
    data['status'] = data.apply(lambda data: statusdict.get(data['status']), axis=1)
    data['businesstype'] = data.apply(lambda data: buinessdict.get(data['businesstype']), axis=1)
    data['registStatus'] = data.apply(lambda data: "从未连线" if data['registStatus'] == None else registStatusedic.get(data['registStatus']) , axis=1)
    data1 = data[['name','businesstype','deviceid','clientName','provincename','cityname','countyname','status','registStatus','maintenancePerson']]
    data1.columns=['地址名称','业务类型','站址CODE','客户名称','省','市','区','站址状态','在线状态','工单处理人']
    cvs_name = './files/站址管理' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.csv'
    #print(data1)
    data1.to_csv(cvs_name, encoding='utf_8_sig', index=None)   # 保存数据
    return data1


def getstationstatus(cookie):

    """获取站址状态列表"""

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',

        'Connection': 'keep-alive',
        'Content-Length': '61',
        'Cookie': cookie,
        'Host': '180.153.49.85:58580',
        'Origin': 'http://180.153.49.85:58580',
        'Pragma': 'no-cache',
        'Referer': 'http://180.153.49.85:58580/station?list&roleId=0001931',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    form_data = {
        'getDictList':"",
        'dictionaryCode':'IDD_STATION_STATUS'
    }
    url ="http://180.153.49.85:58580/baseController?getDictList&dictionaryCode=IDD_STATION_STATUS"
    response = requests.get(url, data=form_data, headers=headers)  # 发起请求
    print(response.status_code)
    f_list = response.json()
    status_dict = {}
    for f_dict in f_list:
        status_dict[f_dict.get('itemCode')] = f_dict.get('itemName')    # 形成新的状态数据字典
    print(status_dict)
    return status_dict


def getbusinesstypedic(cookie):

    """获取业务类型数据字典"""

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',

        'Connection': 'keep-alive',
        'Content-Length': '61',
        'Cookie': cookie,
        'Host': '180.153.49.85:58580',
        'Origin': 'http://180.153.49.85:58580',
        'Pragma': 'no-cache',
        'Referer': 'http://180.153.49.85:58580/station?list&roleId=0001931',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    form_data = {
        'getDictList':"",
        'dictionaryCode':'IDD_BUSINESS_TYPE'
    }
    url ="http://180.153.49.85:58580/baseController?getDictList&dictionaryCode=IDD_BUSINESS_TYPE"
    response = requests.get(url, data=form_data, headers=headers)  # 发起请求
    print(response.status_code)
    business_list = response.json()
    print(business_list)
    buiness_dict = {}
    for b_dict in business_list:
        print(b_dict)
        buiness_dict[b_dict.get('itemCode')]= b_dict.get('itemName')    # 形成新的状态数据字典
    print(buiness_dict)
    return buiness_dict



def getregistStatusedic(cookie):

    """获取在线状态字典"""

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',

        'Connection': 'keep-alive',
        'Content-Length': '61',
        'Cookie': cookie,
        'Host': '180.153.49.85:58580',
        'Origin': 'http://180.153.49.85:58580',
        'Pragma': 'no-cache',
        'Referer': 'http://180.153.49.85:58580/station?list&roleId=0001931',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    form_data = {
        'getDictList':"",
        'dictionaryCode':'IDD_BUSINESS_TYPE'
    }
    url ="http://180.153.49.85:58580/baseController?getDictList&dictionaryCode=IDD_FSU_REGISTSTATUS"
    response = requests.get(url, data=form_data, headers=headers)  # 发起请求
    print(response.status_code)
    business_list = response.json()
    print(business_list)
    buiness_dict = {}
    for b_dict in business_list:
        print(b_dict)
        buiness_dict[b_dict.get('itemCode')]= b_dict.get('itemName')    # 形成新的状态数据字典
    print(buiness_dict)
    return buiness_dict
