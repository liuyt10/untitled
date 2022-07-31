# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : file_upload_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 13:54
# @Copyright: 北京码同学
import requests

url = 'http://www.mtxshop.com:7000/uploaders'

params = {
    'scene':'goods'
}
# 文件参数
files = {
    # file对应的是一个元组
    # 元组的第一个是文件名称
    # 第二个是读取文件的二进制对象
    # 第三个是文件的类型
    'file':('logo.png',open(file=r'C:\Users\lixio\Desktop\logo.png',mode='rb'),'images/png')
}
# 接口调用
resp = requests.post(url=url,params=params,files=files)
print(resp.json())
