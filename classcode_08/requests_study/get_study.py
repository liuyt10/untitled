# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : get_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 11:40
# @Copyright: 北京码同学
import requests

# 要针对一个接口发起请求，需要知道接口的哪些基本信息
# 接口地址、接口请求方式、接口的请求headers、接口的请求参数
url = 'http://www.mtxshop.com:7000/pages/article-categories'
# 查询参数
params = {
    'category_type':'HELP'
}
# 基本信息准备好以后，发起接口调用,拿到响应对象
# resp表示的响应结果对象，包括：响应headers、响应状态码、响应body体信息...
resp = requests.get(url=url,params=params)
# print(resp)
# 从响应对象中获取响应状态码
status = resp.status_code
print(status)
# 获取响应body体信息
text = resp.text # 获取到的结果类型是个字符串，不管接口响应数据格式是纯文本、html、xml、json都可以获取
print(text)
# 以json对象类型的形式得到结果
resp_json = resp.json() # 返回结果类型可能是字典也可能是列表，是什么取决于接口返回的json数据的格式
print(resp_json)
print(type(resp_json))