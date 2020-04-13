# coding=utf-8
from PIL import Image
from selenium import webdriver
import time
from codeapi import getidenticode


def login():

    """自动登录平台获取cookie"""

    driver = webdriver.Firefox()
    driver.get("http://180.153.49.85:58580/welcome.jsp")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_id("loginName").send_keys("scxcj")   # 输入用户名
    driver.find_element_by_id("password").send_keys('123456') # 输入验证码
    driver.find_element_by_id("password").send_keys('')
    element = driver.find_element_by_id('verifyimg')
    time.sleep(2)
    element.screenshot('./codeimg/code.png')
    code = getidenticode('./codeimg/code.png')      # 获取验证码
    driver.find_element_by_id("validateCode").send_keys(code)
    time.sleep(3)

    "判断验证码是否正确"


    driver.find_element_by_id("loginsubmit").click()  # 点击登录
    try:
        value = driver.find_element_by_id("msgWrap").text
        print("++" + value)
    except:
        value = ''

    while value != '':
        element.screenshot('./codeimg/code.png')
        code = getidenticode('./codeimg/code.png')  # 获取验证码
        driver.find_element_by_id("validateCode").clear()
        driver.find_element_by_id("validateCode").send_keys(code)
        time.sleep(3)

        "判断验证码是否正确"

        driver.find_element_by_id("loginsubmit").click()  # 点击登录
        time.sleep(1)
        try:
            value = driver.find_element_by_id("msgWrap").text
        except:
            value =''
        print(value)

    '''JSESSIONID=Xa54eutlhbK3HHhhpTZnIgPKNZ8ZQFCgl2TgMUFX.localhost; __
    SDID=b98b62c492d5f1d1; 
    userName=scxcj; 
    businesstype=2'''

    cookies_list = driver.get_cookies()
    cookies = ''
    print(cookies_list)
    for item in cookies_list:
        name = item.get('name')
        value = item.get('value')
        cookies = cookies + name + '=' + value +';'
    cookies = cookies + 'businesstype=2'
    print(cookies)
    return cookies
    driver.quit()


#login()