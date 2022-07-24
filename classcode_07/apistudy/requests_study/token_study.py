# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : token_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 14:31
# @Copyright: 北京码同学

import requests
# 得到一个session对象，调用多个接口时，使用相同的session对象，会自动帮我们完成cookie关联
# 不能做到token的自动关联
session = requests.session()

url = 'http://82.156.74.26:9088/pinter/bank/api/login2'
data = {
    'userName':'shamo',
    'password':'123456'
}
# resp = requests.post(url=url,data=data)
resp = session.request(method='post',url=url,data=data)
print(resp.json()) # {'code': '0', 'message': 'success', 'data': 'bac4a680fc024e72bb4452da84ee8930'}
# 从登录接口的响应信息中提取token数据，token对应的字段是data
token = resp.json()['data']
print(token)


# 查询余额
url = 'http://82.156.74.26:9088/pinter/bank/api/query2'
# 该接口在调用时，需要传递一个特殊的头信息，头信息参数叫做testfan-token
headers = {
    'testfan-token':token
}
params = {
    'userName':'shamo'
}
# resp = requests.get(url=url,params=params)
resp = session.request(method='get',url=url,params=params,headers=headers)
print(resp.json())


aaa = {
    'code': '0',
    'message': 'success',
    'data': {
        'token':'bac4a680fc024e72bb4452da84ee8930',
        'hshs':'sjhdhd',
        'dsds':'djdj'
    }
}
print(aaa['data']['token'])