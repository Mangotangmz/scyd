import datetime
import requests
import pandas as pd


def getactivealarm(cookie):

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
        'Referer': 'http://www.chinaooc.cn/front/show_index.htm',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    form_data = {
        "page":"1",
        "rows":'1'}
    url = 'http://180.153.49.85:58580/activeAlarm?datagrid'    # 请求地址
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
    data['firstsystemtime'] = pd.to_datetime(data['firstsystemtime'], unit='ms', utc=True)
    data1 = data[['provincename','cityname','countyname','alarmlevel','alarmname','mid',"firstsystemtime",'detailinfo','devname','objid','subobjid','devtablename']]
    data1.columns=['省','市','区','告警等级', '告警名称', '信号量id', '告警发生时间','告警详情','告警设备名称','告警设备id','告警上报设备id','devtablename']
    cvs_name = './files/活动告警监控' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.csv'
    print(data1)
    data1.to_csv(cvs_name, encoding='utf_8_sig', index=None)   # 保存数据
    return data1

