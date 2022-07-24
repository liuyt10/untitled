# -*- coding:utf-8 -*-

import requests


def post():
    url = 'http://82.156.74.26:9088/pinter/com/register'
    json = {
        "userName": "test",
        "password": "1234",
        "gender": 1,
        "phoneNum": "110",
        "email": "rhearh@163.com",
        "address": "测试数据"
    }
    resp = requests.post(url=url, json=json)
    return resp


def put():
    url = 'http://82.156.74.26:9088/pinter/com/phone'
    json = {
        "brand": "Huawei",
        "color": "yellow",
        "memorySize": "64G",
        "cpuCore": "8核",
        "price": "8848",
        "desc": "全新上市"
    }
    resp = requests.put(url=url, json=json)
    return resp


def delete():
    url = 'http://82.156.74.26:9088/pinter/com/phone'
    json = {
        "brand": "Huawei",
        "color": "yellow",
        "memorySize": "64G",
        "cpuCore": "8核",
        "price": "8848",
        "desc": "全新上市"
    }
    resp = requests.delete(url=url, json=json)
    return resp


def file_upload():
    url = 'http://www.mtxshop.com:7000/uploaders'
    param = {
        'scene': 'goods'
    }
    file = r'C:\Users\1\Desktop\码同学\自动化文件\unittest.pdf'
    files = {
        'file': ('unittest.pdf', open(file=file, mode='rb'), 'application/pdf')
    }
    resp = requests.post(url=url, files=files, params=param)
    return resp


session = requests.session()
token = ''


def session_requse(username, uuid, password='e10adc3949ba59abbe56e057f20f883e', captcha='1512'):
    url = 'http://www.mtxshop.com:7002/passport/login'
    headers = {
        'Authorization': ''
    }
    data = {
        'username': username,
        'password': password,
        'captcha': captcha,
        'uuid': uuid
    }
    resp = session.request(method='post', url=url, data=data, headers=headers)
    global token
    token = resp.json()['access_token']
    return resp


def token_request(sku_id, num):
    '''

    :param sku_id:
    :param num:
    :return:
    '''
    url = r'http://www.mtxshop.com:7002/trade/carts/buy'
    header = {
        'Authorization': token
    }
    data = {
        'sku_id': sku_id,
        'num': num
    }
    resp = session.request(method='Post',url=url, headers=header, data=data)
    return resp

if __name__ == '__main__':
    session_requse('shamo', 'dgiagiugera')  # 先进行登录，得到Token
    resp = token_request(2343, 2)  # 传入Token，调用立即购买接口
    print(resp.status_code)
    # print(resp.status_code)
