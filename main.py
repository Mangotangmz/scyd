import datetime
import pandas as pd
from activealarm import getactivealarm
from activedevstatus import get_factorydict, getdevdetail
from historyalram import gethistoryalarmdata, getHistoryfactory
from login import login
from stationaddress import getstationstatus, getstationaddress, getbusinesstypedic, getregistStatusedic

if __name__ == '__main__':
    cookie = login()

    #activealarm= getactivealarm(cookie)  # 获取全部活动告警数据

    """
    factorydict = get_factorydict(activealarm.loc[0, ]["告警上报设备id"], activealarm.loc[0, ]['devtablename'],cookie)    # 获取告警设备厂家数据
    df_dev = pd.DataFrame
    df_dev = activealarm.apply(lambda activealarm: getdevdetail(activealarm['告警上报设备id'], activealarm['devtablename'], factorydict, cookie), axis=1)    #  获取告警设备具体信息
    df_dev = df_dev.apply(pd.Series,index=['设备名称', '设备编码', '市', '区', '创建时间', '设备厂家', '设备型号', '电池状态'])
    cvs_name = './files/告警设备详细信息' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'
    df_dev.to_csv(cvs_name, encoding='utf_8_sig', index=None)           # 设备详细信息转出成csv
    historyfactorydict = getHistoryfactory(cookie)
    history_alarm = gethistoryalarmdata(historyfactorydict, cookie)     # 获取历史告警信息
    """

    station_statusdict = getstationstatus(cookie)                       # 获取地址状态数据字典
    buinessdict = getbusinesstypedic(cookie)                            # 获取业务类数据字典
    registStatusedic = getregistStatusedic(cookie)
    station_address = getstationaddress(cookie, station_statusdict, buinessdict,registStatusedic)     # 获取站址信息

