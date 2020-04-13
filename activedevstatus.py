
import json
import requests


from Utils import timeStamp

#cookie = 'JSESSIONID=VnoYUMhazC5b_7hjoI3tLId3G5zpt-0OqVsSQMKb.localhost; Hm_lvt_f6097524da69abc1b63c9f8d19f5bd5b=1584940770; Hm_lpvt_f6097524da69abc1b63c9f8d19f5bd5b=1585099106; userName=scxcj; businesstype=2'



def getdevdetail(code,devtablename,fatorydict,cookie):

    """获取活动告警具体设备详情"""

    dev_formdata = {
        'code': code
    }
    c = ''

    if devtablename  == 'TW_PW_SWITCH_CABINET':
        c = "dev/TW_PW_SWITCH_CABINET_Info.jsp?&deviceid="+code
    elif devtablename == 'TW_PW_BATTERY':
        c = "dev/TW_PW_BATTERY_Info.jsp?&deviceid=" + code + "&devType=battery"
    elif devtablename == 'TW_PW_BATTERY_PACK':
        c = "dev/TW_PW_BATTERY_Info.jsp?&deviceid=" + code + "&devType=batteryPack"


    Referer = 'http://180.153.49.85:58580/basisrs/' + c
    print(Referer)

    # 请求头
    headers1 = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',

        'Connection': 'keep-alive',
        'Content-Length': '24',
        'Cookie': cookie,
        'Host': '180.153.49.85:58580',
        'Origin': 'http://180.153.49.85:58580',
        'Pragma': 'no-cache',
        'Referer': Referer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    dev_url = 'http://180.153.49.85:58580/newdhperfreal?getDev'
    try:
        dev_response = requests.post(dev_url, data=dev_formdata, headers=headers1)
        if dev_response.status_code == 500:
            print("ip被限制")
    except:
        dev_list = ['', '', '', '', '', '', '', '']

        return dev_list
    for item in json.loads(dev_response.text):

        """分解返回字符串，包含currentUser中信息"""
        item_dict = dict(item)
        # currentUser_dict = dict(item_dict.get('currentUser'))
        dev_name = item_dict .get('name')
        dev_model = item_dict .get('model')
        dev_cityname=item_dict .get('cityname')
        dev_countyname = item_dict.get('countyname')
        dev_code = item_dict.get('factory')
        dev_factory = fatorydict.get(dev_code)
        dev_createtime =item_dict.get('createtime')
        dev_createtime = timeStamp(dev_createtime)



    """获取具体设备状态"""


    path = "/itower/mongo/findSwitchCabinet?devId=CHZD12KTNX190717037&doorId=undefined&tdsourcetag=s_pctim_aiomsg"

    if devtablename  == 'TW_PW_SWITCH_CABINET':
        path = '/itower/mongo/findSwitchCabinet?devId=' + code +'&doorId=undefined&tdsourcetag=s_pctim_aiomsg'
    elif devtablename == 'TW_PW_BATTERY':
        path = "/itower/mongo/findBattery?devId="+ code + "&tdsourcetag=s_pctim_aiomsg"
    elif devtablename == 'TW_PW_BATTERY_PACK':
        path = "/itower/mongo/findBattery?devId=" + code + "&tdsourcetag=s_pctim_aiomsg"
    else:
        path = "/itower/mongo/findBattery?devId=" + code + "&tdsourcetag=s_pctim_aiomsg"



    status_formdata = {
        'path':path
    }

    Referer = 'http://180.153.49.85:58580/basisrs/dev/TW_PW_SWITCH_CABINET_Info.jsp?&deviceid=' +code
    print(Referer)


    stuatus_url = 'http://180.153.49.85:58580/newdhperfreal/getMongoPerf'
    dev_response = requests.post(stuatus_url,status_formdata , headers=headers1)
    print(dev_response.json())
    print(type(dev_response.json()))
    print(dev_response.json().get('obj'))
    mid_list = eval(dev_response.json().get('obj')).get('signalList')

    if devtablename  == 'TW_PW_SWITCH_CABINET'or 'TW_PW_BATTERY_PACK':
        #print(mid_list)
        try:
            for item in mid_list:

                if item.get('mid') == '01108001':   # 通过中间码获取电池状态
                    print(item)

                    stucode = item.get('value')
                    print(stucode)
                    if stucode == '0':
                        status = '移动'

                    elif stucode == '1':
                        status = '静止'
                        print(status)
                    elif stucode == '2':
                        status = '存储'
                    elif stucode == '3':
                        status = '休眠'
                    else:
                        status = '未知'
        except:
            status = '-'


    else:
        status = '-'
    try:
        print(status)
    except:
        status = '- '

    dev_list = [dev_name, code, dev_cityname, dev_countyname, dev_createtime, dev_factory, dev_model, status]

    return dev_list


def get_factorydict(code,devtablename,cookie):

    """获取厂家dict"""


    dev_formdata = {
        'getDictList':'',
    }
    c = ''

    if devtablename  == 'TW_PW_SWITCH_CABINET':
        c = "dev/TW_PW_SWITCH_CABINET_Info.jsp?&deviceid="+code
    elif devtablename == 'TW_PW_BATTERY':
        c = "dev/TW_PW_BATTERY_Info.jsp?&deviceid=" + code + "&devType=battery"
    elif devtablename == 'TW_PW_BATTERY_PACK':
        c = "dev/TW_PW_BATTERY_Info.jsp?&deviceid=" + code + "&devType=batteryPack"

    Referer = 'http://180.153.49.85:58580/basisrs/' + c
    print(Referer)

    # 请求头
    headers1 = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',

        'Connection': 'keep-alive',
        'Content-Length': '24',
        'Cookie': cookie,
        'Host': '180.153.49.85:58580',
        'Origin': 'http://180.153.49.85:58580',
        'Pragma': 'no-cache',
        'Referer': Referer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    facltory_url = "http://180.153.49.85:58580/baseController?getDictList&dictionaryCode=IDD_FSU_FACTORY"
    factory_response = requests.get(facltory_url, data=dev_formdata, headers=headers1)       # 请求厂家数据
    f_list = factory_response.json()
    facltory_dict = {}
    for f_dict in f_list:
        facltory_dict[f_dict.get('itemCode')] = f_dict.get('itemName')    # 形成新的厂家数据字典
    print(facltory_dict)
    return facltory_dict

