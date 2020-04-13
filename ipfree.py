import datetime
import json
import requests

import time
from bs4 import BeautifulSoup

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',

    'Connection': 'keep-alive',
    'Content-Length': '61',
    'Cookie': 'JSESSIONID=b3-Vh8M4nvm1RX5W-59eUmmrYIxSQ8k02BAetzHA.localhost; Hm_lvt_f6097524da69abc1b63c9f8d19f5bd5b=1584940770; Hm_lpvt_f6097524da69abc1b63c9f8d19f5bd5b=1584940865; userName=scxcj; businesstype=2',
    'Host': '180.153.49.85:58580',
    'Origin': 'http://180.153.49.85:58580/basisrs/activeAlarm/allActiveAlarmList.jsp',
    'Pragma': 'no-cache',
    'Referer': 'http://www.chinaooc.cn/front/show_index.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

    'X-Requested-With': 'XMLHttpRequest',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
