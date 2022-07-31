# encoding: utf-8 -*-
import requests

session = requests.session()
token = ''


class buyer_Operate():
    buyer_menu = {'1': 'buy_now', '2': 'create_trade', '3': 'checking_order', '4': 'cancel_order', '5': 'order_rog',
                  '6': 'return_goods', '7': 'submit_comments'}

    def __init__(self):
        self.manager()

    def manager(self):
        print('欢迎进入买家系统，请先进行买家登录操作')
        if self.request_login():
            while True:
                manager_menu = """
                买家可选操作有：
                1.立即购买
                2.创建交易
                3.查询列表
                4.取消订单
                5.确认收货
                6.退货申请
                7.提交评论
                """
                print(manager_menu)
                user_choice = input('请选择以上操作，输入操作对应的数字,输入q退出>>>:'.strip())
                if user_choice == 'q':
                    break
                elif user_choice in buyer_Operate.buyer_menu:
                    try:
                        getattr(self, buyer_Operate.buyer_menu[user_choice])()
                    except Exception as e:
                        print(f"用户进行操作有误，报错原因为：{e}  \n请重新选择操作:")
                        pass
                else:
                    print('操作对应的数字输入错误，请重新输入！！！！')
                    pass

    def request_login(self, uuid='123456', sms_code='908908'):  # 登录用户
        num = input('登录指定账户请输入1，登录默认账户13557047908请输入回车或其他非1的输入：')
        if num == '1':
            mobile = input('请输入需要登录的手机号：')
        else:
            mobile = '13557047908'
        url = f'http://www.mtxshop.com:7002/passport/login/{mobile}'
        print(f'已登录手机号{mobile}')
        headers = {
            'Authorization': ''
        }
        data = {
            'mobile': mobile,
            'sms_code': sms_code,
            'uuid': uuid
        }
        resp = session.request(method='Post', url=url, data=data, headers=headers)
        global token
        try:
            token = resp.json()['access_token']
            print(token)
            print('用户登录成功，请选择所需要的进行的买家操作')
            return resp
        except:
            print('用户登录失败，请查看输入的手机号是否正确')

    @staticmethod
    def buy_now():  # 立即购买，并传入收货地址以及付款方式，可传入sku_id:600
        sku_id = int(input('请输入需要购买的商品对应的sku_id（可传：600）：'))
        num = int(input('请输入需要购买的商品数量：'))
        # 接口基本信息
        buy_now_url = 'http://www.mtxshop.com:7002/trade/carts/buy'  # 立即购买url
        set_paytype_url = f'http://www.mtxshop.com:7002/trade/checkout-params/payment-type'  # 设置支付类型url
        set_addressid_url = f'http://www.mtxshop.com:7002/trade/checkout-params/address-id/6304'  # 添加收货地址url
        headers = {
            'Authorization': token
        }
        buy_now_data = {
            # 注意sku_id并不是商品id，而是商品id所对应的sku_id
            # 数据库里找到mtxshop_goods这库，查询sql：SELECT * FROM `es_goods_sku` WHERE goods_id=17139;
            'sku_id': sku_id,
            'num': num,
            'activity_id': ''
        }
        set_paytype_data = {
            'payment_type': 'COD'  # 默认支付方式为：货到付款
        }
        # 发起接口调用
        buy_now_resp = session.request(method='post', url=buy_now_url, data=buy_now_data, headers=headers)  # 调用立即购买
        set_paytype_resp = session.request(method='post', url=set_paytype_url, data=set_paytype_data,
                                           headers=headers)  # 传入付款方式
        set_addressid_resp = session.request(method='post', url=set_addressid_url, headers=headers)  # 传入收货地址
        assert buy_now_resp.status_code == 200 and set_paytype_resp.status_code == 200 and set_addressid_resp.status_code == 200, '立即购买或付款方式或收货地址接口调用失败'
        print('商品进入立即购买界面，并填写了默认收货地址和付款方式，请输入2进行交易创建')

    @staticmethod
    def create_trade(client='PC', way='BUY_NOW'):  # 创建交易，将缓存与Redis中的交易方式为'BUY_NOW'的订单创建
        # 接口基本信息
        url = f'http://www.mtxshop.com:7002/trade/create'
        headers = {
            'Authorization': token
        }
        data = {
            'client': client,
            'way': way
        }
        # 发起接口调用
        resp = session.request(method='post', url=url, data=data, headers=headers)
        assert resp.status_code == 200, f'创建订单接口调用失败:{resp.json()}'
        print(
            f'交易创建成功,等待卖家发货,订单编号为{resp.json()["order_list"][0]["sn"]},商品总价格为：{resp.json()["price_detail"]["total_price"]},sku_id为：{resp.json()["order_list"][0]["sku_list"][0]["sku_id"]}')  # 返回响应对象，提供给调用方使用

    @staticmethod
    def checking_order(page_no=1, page_size=10):  # 查询订单
        key_words = input('请输入需要查询的订单关键字：')
        order_status = input('请输入需要查询的订单状态：')
        url = r'http://www.mtxshop.com:7002/trade/orders'
        header = {
            'Authorization': token
        }
        params = {
            'key_words': key_words,
            'order_status': order_status,
            'page_no': page_no,
            'page_size': page_size
        }
        resp = session.request(method='get', headers=header, url=url, params=params)
        assert resp.status_code == 200, f'订单查询接口调用失败:{resp.json()}'
        print(f'返回的订单信息为：\n{resp.text}')

    @staticmethod
    def cancel_order():  # 取消订单
        order_sn = input('请输入需要取消的订单编号：')
        reason = input('请输入取消订单的原因：')
        url = f'http://www.mtxshop.com:7002/trade/orders/{order_sn}/cancel'
        header = {
            'Authorization': token
        }
        data = {
            'order_sn': order_sn,
            'reason': reason
        }
        resp = session.request(method='post', url=url, headers=header, data=data)
        assert resp.status_code == 200, f'订单取消接口调用失败:{resp.json()}'
        print(f'会员创建的订单号{order_sn}已经被取消，取消原因是{reason}')

    @staticmethod
    def order_rog():  # 确认收货
        order_sn = input('请输入待收货的订单编号：')
        url = f'http://www.mtxshop.com:7002/trade/orders/{order_sn}/rog'
        header = {
            'Authorization': token
        }
        data = {
            'order_sn': order_sn
        }
        resp = session.request(method='post', url=url, headers=header, data=data)
        assert resp.status_code == 200, f'订单确认收货接口调用失败:{resp.json()}'
        print('商品已收货成功，等待卖家确认收款')

    @staticmethod
    def return_goods():  # 退货申请
        order_sn = input('请输入需要退货的订单编号：')  # 20220726000397
        sku_id = input('请输入需要退货的订单sku_id:')  # 600
        # 接口基本信息
        url = f'http://www.mtxshop.com:7002/after-sales/apply/return/goods'
        headers = {
            'Authorization': token
        }
        data = {
            'service_type': 'RETURN_GOODS',
            'images': 'http://www.mtxshop.com:7000/statics/attachment/normal/2022/7/24/9/58263306.png',
            'return_num': 1,
            'ship_addr': '北京霍营',
            'ship_name': '沙陌',
            'ship_mobile': '18729399607',
            'account_type': 'BANKTRANSFER',
            'bank_name': '沙陌银行',
            'bank_deposit_name': '北京分行',
            'bank_account_name': '沙陌',
            'bank_account_number': '7272634623464',
            'reason': '发错货',
            'problem_desc': '不想说啥了，就想退',
            'order_sn': order_sn,
            'sku_id': sku_id,
            'apply_vouchers': '',
            'region': 2799,
        }

        resp = session.request(method='post', url=url, data=data, headers=headers)
        assert resp.status_code == 200, f'订单申请退货接口调用失败:{resp.json()}'
        print('商品已退货成功，费用已经原路返回')

    @staticmethod
    def submit_comments():  # 提交评论
        sku_id = input('请输入需要提交评论的商品对应的sku_id：')
        order_sn = input('请输入提交评论的订单编号：')
        content = input('请输入需要提交的评论内容：')
        url = f'http://www.mtxshop.com:7002/members/comments'
        header = {
            'Authorization': token
        }
        json = {
            "comments": [
                {
                    "content": content,
                    "grade": "good",
                    "images": [
                        "无"
                    ],
                    "sku_id": sku_id  # 2728
                }
            ],
            "delivery_score": 5,
            "description_score": 5,
            "order_sn": order_sn,  # 20220721000516
            "service_score": 5
        }
        resp = session.request(method='post', url=url, headers=header, json=json)
        assert resp.status_code == 200, f'提交评论接口调用失败{resp.json()}'
        print(f'用户对订单{order_sn}的评论已经提交')
