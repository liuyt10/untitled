# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : post_form_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 13:33
# @Copyright: 北京码同学

import requests

# post 表单接口
url = 'http://www.mtxshop.com:7002/passport/login'
headers = {
    'Authorization':''
}
# params = {
#     'username':'shamo',
#     'password':'e10adc3949ba59abbe56e057f20f883e',
#     'captcha':'1512',
#     'uuid':'sdhhjshjdhdhd'
# }
data = {
    'username':'shamo',
    'password':'e10adc3949ba59abbe56e057f20f883e',
    'captcha':'1512',
    'uuid':'sdhhjshjdhdhd'
}
# 发起接口调用，拿到响应对象
# resp = requests.post(url=url,params=params,headers=headers)
resp = requests.post(url=url,data=data,headers=headers)
# 获取响应状态码
status_code = resp.status_code
print(status_code)
# 获取响应body体信息
resp_json = resp.json()
print(resp_json)
