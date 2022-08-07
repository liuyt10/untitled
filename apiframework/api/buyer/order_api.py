# -*- coding:utf-8 -*-
from api.base_api import BaseBuyerApi
from api.buyer.buyer_login_api import BuyerLoginApi


class CreatTradeApi(BaseBuyerApi):  # 创建交易
    def __init__(self, client='PC', way='BUY_NOW'):
        super().__init__()
        self.url = f'{self.host}/trade/create'
        self.method = 'post'
        self.data = {
            'client': client,
            'way': way
        }


# 查询订单
class SearchOrderApi(BaseBuyerApi):
    def __init__(self, order_status='', key_words='沙陌', start_time='', end_time=''):
        super().__init__()
        self.url = f'{self.host}/trade/orders'
        self.method = 'get'
        self.params = {
            'order_status': order_status,
            'page_no': 1,
            'page_size': 5,
            'key_words': key_words,
            'start_time': start_time,
            'end_time': end_time
        }


# 取消订单
class CancelOrderApi(BaseBuyerApi):
    def __init__(self, order_sn, reason='不想要了'):
        super().__init__()
        self.url = f'{self.host}/trade/orders/{order_sn}/cancel'
        self.method = 'post'
        self.data = {
            'reason ': reason
        }


# 确认收获
class OrderRogApi(BaseBuyerApi):
    def __init__(self, order_sn):
        super().__init__()
        self.url = f'{self.host}/trade/orders/{order_sn}/rog'
        self.method = 'post'
        self.data = {
            'order_sn': order_sn
        }


if __name__ == '__main__':
    buyer_login_api = BuyerLoginApi()
    resp = buyer_login_api.send()
    BaseBuyerApi.buyer_token = resp.json()['access_token']
    # creat_trade_api = CreatTradeApi()
    # resp = creat_trade_api.send()
    # print(resp.json())
    # print(resp.json()["order_list"][0]["sn"])
    # order_rog_api = OrderRogApi(20220805000002)
    # resp = order_rog_api.send()
    # print(resp.status_code)
    search_order_api = SearchOrderApi()
    search_order_resp = search_order_api.send()
    print(search_order_resp.json())
