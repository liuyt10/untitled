# encoding: utf-8 -*-

import requests

session = requests.session()
token = ''


class seller_Operate():
    seller_menu = {'1': 'add_goods', '2': 'modify_product', '3': 'order_shipped', '4': 'confirmed_paid'}

    def __init__(self):
        self.manager()

    def manager(self):
        print('欢迎进入卖家系统，已经登录默认卖家账号：shamoseller')
        if self.request_login():
            while True:
                manager_menu = """
                卖家可选操作有：
                1.添加商品
                2.修改商品
                3.订单发货
                4.确认收款
                """
                print(manager_menu)
                user_choice = input('请选择以上操作，输入操作对应的数字,输入q退出>>>:'.strip())
                if user_choice == 'q':
                    break
                elif user_choice in seller_Operate.seller_menu:
                    getattr(self, seller_Operate.seller_menu[user_choice])()
                else:
                    print('操作对应的数字输入错误，请重新输入！！！！')
                    pass

    def request_login(self):  # 登录用户
        url = f'http://www.mtxshop.com:7002/passport/login'
        headers = {
            'Authorization': ''
        }
        data = {
            'username': 'shamoseller',
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'captcha': 1512,
            'uuid': '456781'

        }
        resp = session.request(method='post', url=url, data=data, headers=headers)
        global token
        try:
            token = resp.json()['access_token']
            print(token)
            print('用户登录成功，请选择所需要的进行的买家操作')
            return resp
        except:
            print('用户登录失败，请查看输入的手机号是否正确')

    @staticmethod
    def add_goods():  # 添加商品
        goods_name = input('请输入商品名称：')
        goods_sn = int(input('请输入需要添加的商品编号：'))
        price = int(input('请输入商品价格：'))
        quantity = int(input('请输入商品库存：'))
        weight = float(input('请输入商品重量：'))
        url = f'http://www.mtxshop.com:7003/seller/goods'
        header = {
            'Authorization': token
        }
        json = {
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
            "price": price,
            "quantity": quantity,
            "shop_cat_id": 98,
            "sku_list": [],
            "sn": goods_sn,
            "template_id": 0,
            "weight": weight
        }
        resp = session.request(method='post', url=url, headers=header, json=json)
        assert resp.status_code == 200, f'添加商品接口调用失败:{resp.json()}'
        print(f'商品id为：{resp.json()["goods_id"]}，商品添加成功')

    @staticmethod
    def modify_product():  # 修改商品
        id = int(input('请输入需要修改的商品id：'))
        price = int(input('请输入新的价格：'))
        goods_name = input('请输入新的商品名称：')
        goods_sn = input('请输入新的商品编号：')
        url = f'http://www.mtxshop.com:7003/seller/goods/{id}'
        header = {
            'Authorization': token
        }
        json = {
            "price": price,
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
        resp = session.request(method='put', url=url, headers=header, json=json)
        assert resp.status_code == 200, f'修改商品接口调用失败:{resp.json()}'
        print(f'商品{id}修改成功，新的商品编号为{goods_sn}')

    @staticmethod
    def order_shipped():  # 订单发货
        order_sn = input('请输入需要发货的订单编号：')
        ship_no = input('请输入发货单号：')
        url = f'http://www.mtxshop.com:7003/seller/trade/orders/{order_sn}/delivery'
        header = {
            'Authorization': token
        }
        data = {
            'order_sn': order_sn,
            'ship_no': ship_no,
            'logi_id': '13',
            'logi_name': '中通01'
        }
        resp = session.request(method='post', url=url, headers=header, data=data)
        assert resp.status_code == 200, f'订单发货接口调用失败:{resp.json()}'
        print(f'订单{order_sn}发货成功，用户可以确认收货')

    @staticmethod
    def confirmed_paid():  # 确认收款
        order_sn = input('请输入需要收款的订单编号：')
        pay_price = int(input('请输入付款金额：'))
        url = f'http://www.mtxshop.com:7003/seller/trade/orders/{order_sn}/pay'
        header = {
            'Authorization': token
        }
        data = {
            'order_sn': order_sn,
            'pay_price': pay_price
        }
        resp = session.request(method='post', url=url, headers=header, data=data)
        assert resp.status_code == 200, f'订单确认收款接口调用失败：{resp.json()}'
        print('订单确认收款成功，用户可申请退货或提交评论')
