import datetime
import requests

import pandas as pd

from Utils import timeStamp


#cookie = 'JSESSIONID=WdT_Xf3lydKvcVFu9fxmqGHDMVX6tXIS94At0JAk.localhost; __SDID=effb237b7afa91ff; userName=scxcj; businesstype=2'


def gethistoryalarmdata(fatorydict,cookie):

    """获取告警数据"""

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
        'Referer': 'http://180.153.49.85:58580/basisrs/alarmHistory/businessTwPwAlarmHistoryList.jsp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    form_data = {
        'businesstype':"2",
        "page":"1",
        "rows":'1'}
    url = 'http://180.153.49.85:58580/alarmHistory?datagrid'    # 请求地址
    response = requests.post(url, data=form_data, headers=headers)  # 发起请求
    print(response.json())
    print(response.json().get("total"))   # 获取返回数据条数
    #rows = str(response.json().get("total"))
    rows =30
    '''===========第二次获取全部数据=========='''
    form_data = {
        "page": "1",
        "rows": rows
    }

    response = requests.post(url, data=form_data, headers=headers)   # 发起请求
    print(response.json().get("total"))
    rowslist1 = response.json().get("rows")   # 获取返回数据
    data = pd.DataFrame(rowslist1)
    data['lasttime'] = (data['clearsystemtime']-data['firstsystemtime'])/1000/60
    data['lasttime'] = data.apply(lambda data: format(data['lasttime'], '.1f'), axis=1)
    data['clearsystemtime'] = data.apply(lambda data: timeStamp(data['clearsystemtime']), axis=1)
    data['firstsystemtime'] = data.apply(lambda data: timeStamp(data['firstsystemtime']), axis=1)
    data['devstyle'] = '换电柜'
    data['factory'] = data.apply(lambda data:fatorydict.get(data['factory']),axis=1)
    data1 = data[['provincename','cityname','countyname','alarmlevel','alarmname',"firstsystemtime",'clearsystemtime','clearcause','lasttime','detailinfo','devname','objid','devstyle','factory']]
    data1.columns=['省','市','区','告警等级', '告警名称', '告警发生时间','告警清除时间','告警清除原因','告警历时','告警详情','告警设备名称','告警设备编码','设备类型','设备厂家']
    cvs_name = './files/历史告警监控' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.csv'
    #print(data1)
    data1.to_csv(cvs_name, encoding='utf_8_sig', index=None)   # 保存数据
    return data1


def getHistoryfactory(cookie):

    """获取告警数据厂家课表"""

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
        'Referer': 'http://180.153.49.85:58580/basisrs/alarmHistory/businessTwPwAlarmHistoryList.jsp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    form_data = {
        'getDictList':"",
        'dictionaryCode':'IDD_FSU_FACTORY'
    }
    url ="http://180.153.49.85:58580/baseController?getDictList&dictionaryCode=IDD_FSU_FACTORY"
    response = requests.get(url, data=form_data, headers=headers)  # 发起请求
    print(response.status_code)
    f_list = response.json()
    facltory_dict = {}
    for f_dict in f_list:
        facltory_dict[f_dict.get('itemCode')] = f_dict.get('itemName')    # 形成新的厂家数据字典
    #print(facltory_dict)
    return facltory_dict
