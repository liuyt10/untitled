# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : put_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 13:51
# @Copyright: 北京码同学


import requests


url = 'http://82.156.74.26:9088/pinter/com/phone'
json = {"brand":"Huawei","color":"yellow","memorySize":"64G","cpuCore":"8核","price":"8848","desc":"全新上市"}
# 发起接口调用
resp = requests.put(url=url,json=json)
print(resp.status_code)
print(resp.json())