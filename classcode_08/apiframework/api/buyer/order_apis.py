# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : order_apis.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 14:02
# @Copyright: 北京码同学
from api.base_api import BaseBuyerApi


class CreateTradeApi(BaseBuyerApi):

    def __init__(self,client='PC',way='BUY_NOW'):
        super().__init__()
        self.url = f'{self.host}/trade/create'
        self.method = 'post'
        self.data = {
            'client':client,
            'way':way
        }
class SearchOrderApi(BaseBuyerApi):

    def __init__(self,order_status='',key_words='沙陌',start_time=1657987200,end_time=1658505599):
        super().__init__()
        self.url = f'{self.host}/trade/orders'
        self.method = 'get'
        self.params = {
            'order_status':order_status,
            'page_no':1,
            'page_size':5,
            'key_words':key_words,
            'start_time':start_time,
            'end_time':end_time

        }
class CancelOrderApi(BaseBuyerApi):

    def __init__(self,order_sn,reason='没啥原因就是不想要了'):
        super().__init__()
        self.url = f'{self.host}/trade/orders/{order_sn}/cancel'
        self.method = 'post'
        self.data = {
            'reason ':reason
        }