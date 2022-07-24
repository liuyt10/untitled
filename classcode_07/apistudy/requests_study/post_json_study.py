# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : post_json_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 13:42
# @Copyright: 北京码同学

import requests


url = 'http://82.156.74.26:9088/pinter/com/register'
json = {
    "userName":"test",
    "password":"1234",
    "gender":1,
    "phoneNum":"110",
    "email":"beihe@163.com",
    "address":"Beijing"
}
# 发起接口调用
resp = requests.post(url=url,json=json)
print(resp.status_code)
print(resp.json())