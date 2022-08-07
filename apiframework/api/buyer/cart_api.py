# -*- coding:utf-8 -*-
from api.base_api import BaseBuyerApi
from api.buyer.buyer_login_api import BuyerLoginApi


# 购物车立即购买
class BuyNowApi(BaseBuyerApi):
    def __init__(self, sku_id=600, num=1):  # 商品sku_id可以传入600
        super().__init__()
        self.url = f'{self.host}/trade/carts/buy'
        self.method = 'post'
        self.data = {
            # 注意sku_id并不是商品id，而是商品id所对应的sku_id
            # 数据库里找到mtxshop_goods这库，查询sql：SELECT * FROM `es_goods_sku` WHERE goods_id=17139;
            'sku_id': sku_id,
            'num': num,
            'activity_id': ''
        }


# 添加到购物车
class AddCartApi(BaseBuyerApi):
    def __init__(self, sku_id=17418, num=1):  # 商品sku_id可以传入600
        super().__init__()
        self.url = f'{self.host}/trade/carts'
        self.method = 'post'
        self.data = {
            # 注意sku_id并不是商品id，而是商品id所对应的sku_id
            # 数据库里找到mtxshop_goods这库，查询sql：SELECT * FROM `es_goods_sku` WHERE goods_id=17139;
            'sku_id': sku_id,
            'num': num,
            'activity_id': ''
        }


# 清空购物车
class DelectableApi(BaseBuyerApi):
    """
       情况购物车数据，其实就是清空了redis里的购物车数据
       :return:
       """
    def __init__(self):
        super().__init__()
        # 接口基本信息
        self.url = f'{self.host}/trade/carts'
        self.method = 'delete'


if __name__ == '__main__':
    buyer_login_api = BuyerLoginApi()
    resp = buyer_login_api.send()
    BaseBuyerApi.buyer_token = resp.json()['access_token']
    buy_now_api = BuyNowApi()
    print(buy_now_api.headers)
    resp = buy_now_api.send()
    print(resp.status_code)
