# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : client.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 11:42
# @Copyright: 北京码同学
import requests

# 注意这个类是所有接口封装时的父类
from common.encry_decry import AesEncrypt


class RequestsClient:
    session = requests.session()#使用类属性来定一个session，他将作为所有接口发起的全局对象

    def __init__(self):
        self.session = RequestsClient.session
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.files = None
        self.resp = None
        # 假如你要做aes加解密
        self.aes = AesEncrypt(key='0123456789123456')

    def send(self,**kwargs):
        # 如果调用方，没有传任何的参数，那么就使用该对象的默认属性参数
        if 'url' not in kwargs:
            kwargs['url'] = self.url
        if 'method' not in kwargs:
            kwargs['method'] = self.method
        if 'headers' not in kwargs:
            kwargs['headers'] = self.headers
        if 'params' not in kwargs:
            kwargs['params'] = self.params
        if 'data' not in kwargs:
            kwargs['data'] = self.data
        if 'json' not in kwargs:
            kwargs['json'] = self.json
        if 'files' not in kwargs:
            kwargs['files'] = self.files
        # 发起之前针对所有的参数进行加密处理
        # data = self.aes.encrypt(kwargs)
        # kwargs['data'] = data
        self.resp = self.session.request(**kwargs)
        # 解密数据
        # data = self.aes.decrypt(self.resp.text)
        return self.resp
if __name__ == '__main__':
    # 登录接口
    r = RequestsClient()
    r.send(method='post',url='',data='')
