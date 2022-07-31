# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : base_api.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 13:42
# @Copyright: 北京码同学
from common.client import RequestsClient


class BaseBuyerApi(RequestsClient):
    buyer_token = '' #初始定义是个空值，那么在整个框架层面，必须先完成该属性的赋值
    uid = ''
    def __init__(self):
        super().__init__()
        self.host = 'http://www.mtxshop.com:7002'
        self.headers = {
            'Authorization': BaseBuyerApi.buyer_token
        }
class BaseSellerApi(RequestsClient):
    seller_token = '' #初始定义是个空值，那么在整个框架层面，必须先完成该属性的赋值
    def __init__(self):
        super().__init__()
        self.host = 'http://www.mtxshop.com:7003'
        self.headers = {
            'Authorization': BaseSellerApi.seller_token
        }
class BaseManagerApi(RequestsClient):
    manager_token = '' #初始定义是个空值，那么在整个框架层面，必须先完成该属性的赋值
    def __init__(self):
        super().__init__()
        self.host = 'http://www.mtxshop.com:7004'
        self.headers = {
            'Authorization': BaseManagerApi.manager_token
        }
class BaseBasicApi(RequestsClient):
    def __init__(self):
        super().__init__()
        self.host = 'http://www.mtxshop.com:7000'