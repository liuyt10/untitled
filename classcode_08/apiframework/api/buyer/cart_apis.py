# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : cart_apis.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 13:33
# @Copyright: 北京码同学
from api.base_api import BaseBuyerApi
from api.buyer.buyer_login_apis import BuyerLoginApi
from common.client import RequestsClient


class BuyNowApi(BaseBuyerApi):

    def __init__(self,sku_id,num=1):
        super().__init__()
        self.url = f'{self.host}/trade/carts/buy'
        self.method = 'post'
        # self.headers = {
        #     'Authorization': token
        # }
        self.data = {
            # 注意sku_id并不是商品id，而是商品id所对应的sku_id
            # 数据库里找到mtxshop_goods这库，查询sql：SELECT * FROM `es_goods_sku` WHERE goods_id=17139;
            'sku_id': sku_id,
            'num': num,
            'activity_id': ''
        }
class AddCartApi(BaseBuyerApi):

    def __init__(self,sku_id,num=1):
        super().__init__()
        self.url = f'{self.host}/trade/carts'
        self.method = 'post'
        # self.headers = {
        #     'Authorization': token
        # }
        self.data = {
            # 注意sku_id并不是商品id，而是商品id所对应的sku_id
            # 数据库里找到mtxshop_goods这库，查询sql：SELECT * FROM `es_goods_sku` WHERE goods_id=17139;
            'sku_id': sku_id,
            'num': num,
            'activity_id': ''
        }

class DeleteCartApi(BaseBuyerApi):

    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/trade/carts'
        self.method = 'delete'
if __name__ == '__main__':
    buyer_login_api = BuyerLoginApi()
    resp = buyer_login_api.send()
    BaseBuyerApi.buyer_token = resp.json()['access_token']
    buy_now_api = BuyNowApi(sku_id=17418)
    print(buy_now_api.headers)
    resp = buy_now_api.send()
    print(resp.status_code)