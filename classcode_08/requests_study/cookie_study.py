# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : cookie_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 14:24
# @Copyright: 北京码同学

import requests
# 得到一个session对象，调用多个接口时，使用相同的session对象，会自动帮我们完成cookie关联
session = requests.session()

url = 'http://82.156.74.26:9088/pinter/bank/api/login'
data = {
    'userName':'shamo',
    'password':'123456'
}
# resp = requests.post(url=url,data=data)
resp = session.request(method='post',url=url,data=data)
print(resp.json())

# 查询余额
url = 'http://82.156.74.26:9088/pinter/bank/api/query'
params = {
    'userName':'shamo'
}
# resp = requests.get(url=url,params=params)
resp = session.request(method='get',url=url,params=params)
print(resp.json())