# encoding:utf-8

import requests
import base64
import requests
import re

def getidenticode(imgpath):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=jeo6DrC2G56gc54RgXTPNFSv&client_secret=EeyqWs6R6oRSFqxaic9N3sk5TFiRRC5S'
    response = requests.get(host).json()
    print(response['access_token'])

    # if response:
    #     print(response.json())
    #

    '''
    网络图片文字识别(例如：验证码等)
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"
    # 二进制方式打开图片文件
    f = open(imgpath, 'rb')
    img = base64.b64encode(f.read())
    # print(img)

    params = {"image":img}
    access_token = response['access_token']
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        text = response.json()
        word = text['words_result']
        pattern = re.compile('{\'words\': \'(\d+)\'}',re.S)
        value = str(word)
        print(str(word[0]).split('\'')[3])
        return str(word[0]).split('\'')[3]