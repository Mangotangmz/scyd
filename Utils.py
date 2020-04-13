import time

def timeStamp(timeNum):

    """将时间戳转换成普通格式"""

    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


def makeheder(cookie, referer):

    """生成头部"""

    headers= {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',

        'Connection': 'keep-alive',
        'Content-Length': '24',
        'Cookie': cookie,
        'Host': '180.153.49.85:58580',
        'Origin': 'http://180.153.49.85:58580',
        'Pragma': 'no-cache',
        'Referer': referer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

        'X-Requested-With': 'XMLHttpRequest',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    return headers