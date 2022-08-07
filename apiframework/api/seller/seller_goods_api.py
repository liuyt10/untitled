# -*- coding:utf-8 -*-
from api.base_api import BaseSellerApi
from api.seller.seller_login_api import SellerLoginApi


class AddGoodsApi(BaseSellerApi):  # 添加商品
    def __init__(self, goods_name, goods_sn):  # 传入商品名称和商品编号
        super().__init__()
        self.url = f'{self.host}/seller/goods'
        self.method = 'post'
        self.json = {
            "brand_id": "",
            "category_id": 83,
            "category_name": "string",
            "cost": 200,
            "exchange": {
                "category_id": "",
                "enable_exchange": 0,
                "exchange_money": 0,
                "exchange_point": 0
            },
            "goods_gallery_list": [
                {
                    "img_id": -1,
                    "original": "http://www.mtxshop.com:7000/statics/attachment/goods/2022/7/26/11/19215203.jpeg",
                    "sort": 0
                }
            ],
            "goods_name": goods_name,
            "goods_params_list": [],
            "goods_transfee_charge": 1,
            "has_changed": 0,
            "intro": "质量感人肺腑，一定要买",
            "market_enable": 1,
            "meta_description": "",
            "meta_keywords": "",
            "mktprice": "789",
            "page_title": "",
            "price": 180.0,
            "quantity": 200,
            "shop_cat_id": 98,
            "sku_list": [],
            "sn": goods_sn,
            "template_id": 0,
            "weight": 2.5
        }


class ModifyProductApi(BaseSellerApi):  # 修改商品
    def __init__(self, id, goods_name, goods_sn):  # 传入需要修改的商品id，传入新的商品名称和编号
        super().__init__()
        self.url = f'{self.host}/seller/goods/{id}'
        self.method = 'put'
        self.json = {
            "price": 180.0,
            "goods_transfee_charge": 1,
            "goods_type": "NORMAL",
            "market_enable": 1,
            "mktprice": 756,
            "meta_description": "新型智能炒锅",
            "meta_keywords": "新型智能炒锅",
            "goods_gallery_list": [
                {
                    "img_id": 20962,
                    "original": "http://www.mtxshop.com:7000/statics/attachment/goods/2022/7/26/11/19215203.jpeg",
                    "small": "http://www.mtxshop.com:7000/statics/attachment/goods/2022/7/26/11/19215203.jpeg_400x400.jpeg",
                    "thumbnail": "http://www.mtxshop.com:7000/statics/attachment/goods/2022/7/26/11/19215203.jpeg_300x300.jpeg",
                    "sort": 0

                }
            ],
            "goods_name": goods_name,
            "template_id": 0,
            "have_spec": 0,
            "is_auth": 0,
            "promotion_tip": "",
            "category_name": "厨房用品&gt;锅具水壶 &gt;炒锅",
            "category_ids": [79, 80, 83],
            "category_id": 83,
            "cost": 200,
            "quantity": 200,
            "weight": 2.5,
            "sn": goods_sn,
            "shop_cat_id": 98
        }


class OrderShippedApi(BaseSellerApi):  # 订单发货
    def __init__(self, order_sn, ship_no='123445'):  # 商品编号和发货单号
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/delivery'
        self.method = 'post'
        self.data = {
            'order_sn': order_sn,
            'ship_no': ship_no,
            'logi_id': '13',
            'logi_name': '中通01'
        }


class ConfirmedPaid(BaseSellerApi):  # 确认收款
    def __init__(self, order_sn, pay_price):  # 商品编号，订单价格
        super().__init__()
        self.url = f'{self.host}/seller/trade/orders/{order_sn}/pay'
        self.method = 'post'
        self.data = {
            'order_sn': order_sn,
            'pay_price': pay_price
        }


if __name__ == '__main__':
    seller_login_api = SellerLoginApi()
    resp = seller_login_api.send()
    BaseSellerApi.seller_token = resp.json()['access_token']
    add_goods_api = AddGoodsApi('欢欢喜喜组织部', 12553464)
    add_goods_resp = add_goods_api.send()
    id = add_goods_resp.json()['goods_id']
    print(id)
    # goods_sn = add_goods_resp.json()['sn']
    # modify_product_api = ModifyProductApi(id, '修改后商品名称', goods_sn)
    # modify_product_resp = modify_product_api.send()
    # print(modify_product_resp.json())
    # order_ship_api = OrderShippedApi(20220804000620, 34644)
    # order_ship_resp = order_ship_api.send()
    # print(order_ship_resp.status_code)
    # confirmed_paid_api = ConfirmedPaid(20220805000002, 180)
    # resp = confirmed_paid_api.send()
    # print(resp.status_code)
