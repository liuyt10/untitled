# -*- coding:utf-8 -*-
import requests


# 注意这个类是所有接口封装时的父类
class RequestClient:

    def __init__(self):
        self.session = requests.session()  # 使用类属性来定一个session，它将作为所有接口发起的全局对象
        self.url = None
        self.method = None
        self.headers = None
        self.data = None
        self.params = None
        self.json = None
        self.files = None
        self.resp = None

    def send(self, **kwargs):
        # 如果调用方，没有传任何的参数，那么就是用该对象的默认属性参数
        if 'url' not in kwargs:
            kwargs['url'] = self.url
        if 'method' not in kwargs:
            kwargs['method'] = self.method
        if 'headers' not in kwargs:
            kwargs['headers'] = self.headers
        if 'data' not in kwargs:
            kwargs['data'] = self.data
        if 'params' not in kwargs:
            kwargs['params'] = self.params
        if 'json' not in kwargs:
            kwargs['json'] = self.json
        if 'files' not in kwargs:
            kwargs['files'] = self.files
        self.resp = self.session.request(**kwargs)
        return self.resp


if __name__ == '__main__':
    # 登录接口
    r = RequestClient()
    r.send()
