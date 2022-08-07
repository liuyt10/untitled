# -*- coding:utf-8 -*-
from api.buyer.buyer_login_api import BuyerLoginApi
from comment.client import RequestClient


# 买家的服务
class BaseBuyerApi(RequestClient):
    buyer_token = ''  # 初始定义是个空值，那么整个框架层面，必须先完成该属性的赋值

    def __init__(self):
        super().__init__()
        self.host = 'http://www.mtxshop.com:7002'
        self.headers = {
            'Authorization': BaseBuyerApi.buyer_token
        }


# 卖家的服务
class BaseSellerApi(RequestClient):
    seller_token = ''  # 初始定义是个空值，那么整个框架层面，必须先完成该属性的赋值

    def __init__(self):
        super().__init__()
        self.host = 'http://www.mtxshop.com:7003'
        self.headers = {
            'Authorization': BaseSellerApi.seller_token
        }



# 管理员的服务
class BaseManagerApi(RequestClient):
    manager_token = ''  # 初始定义是个空值，那么整个框架层面，必须先完成该属性的赋值

    def __init__(self):
        super().__init__()
        self.host = 'http://www.mtxshop.com:7004'
        self.headers = {
            'Authorization': BaseManagerApi.manager_token
        }

