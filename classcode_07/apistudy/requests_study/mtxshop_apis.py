# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : mtxshop_apis.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 14:43
# @Copyright: 北京码同学
import requests

session = requests.session()
token = ''


# 买家登录接口
def buyer_login(username='shamo', password='e10adc3949ba59abbe56e057f20f883e', captcha='1512'):
    # 接口基本信息
    url = 'http://www.mtxshop.com:7002/passport/login'
    headers = {
        'Authorization': ''
    }
    data = {
        'username': username,
        'password': password,
        'captcha': captcha,
        'uuid': 'sdhhjshjdhdhd'
    }
    # 发起接口调用
    resp = session.request(method='post', url=url, data=data, headers=headers)
    global token  # 声明下面用的这个token，是一个全局的
    token = resp.json()['access_token']
    return resp  # 返回响应对象，提供给调用方使用


def buy_now(sku_id=17418, num=1):
    """
    立即购买接口，业务成功时，响应body体信息是空的.
    成功后会将订单信息存入redis缓存中，这个接口并不是真正的下单
    :param sku_id:
    :param num:
    :return:
    """
    # 接口基本信息
    url = 'http://www.mtxshop.com:7002/trade/carts/buy'
    headers = {
        'Authorization': token
    }
    data = {
        # 注意sku_id并不是商品id，而是商品id所对应的sku_id
        # 数据库里找到mtxshop_goods这库，查询sql：SELECT * FROM `es_goods_sku` WHERE goods_id=17139;
        'sku_id': sku_id,
        'num': num,
        'activity_id': ''
    }
    # 发起接口调用
    resp = session.request(method='post', url=url, data=data, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


def add_cart(sku_id=17418, num=1):
    """
    添加购物车接口，业务成功时，响应body体信息是有内容.
    成功后会将购物车相关信息存入redis缓存中，这个接口并不是真正的下单
    :param sku_id:
    :param num:
    :return:
    """
    # 接口基本信息
    url = 'http://www.mtxshop.com:7002/trade/carts'
    headers = {
        'Authorization': token
    }
    data = {
        # 注意sku_id并不是商品id，而是商品id所对应的sku_id
        # 数据库里找到mtxshop_goods这库，查询sql：SELECT * FROM `es_goods_sku` WHERE goods_id=17139;
        'sku_id': sku_id,
        'num': num,
        'activity_id': ''
    }
    # 发起接口调用
    resp = session.request(method='post', url=url, data=data, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


def delete_cart():
    """
    情况购物车数据，其实就是清空了redis里的购物车数据
    :return:
    """
    # 接口基本信息
    url = 'http://www.mtxshop.com:7002/trade/carts'
    headers = {
        'Authorization': token
    }
    # 发起接口调用
    resp = session.request(method='delete', url=url, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


def set_addressid(address_id=6304):
    """
    该接口是设置订单收货地址，将数据存入到redis缓存中
    业务成功时响应数据是空的
    :param address_id:
    :return:
    """
    # 接口基本信息
    url = f'http://www.mtxshop.com:7002/trade/checkout-params/address-id/{address_id}'
    headers = {
        'Authorization': token
    }
    # 发起接口调用
    resp = session.request(method='post', url=url, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


def set_paytype(payment_type='COD'):
    """
    该接口是设置订单的支付类型，将数据存入到redis缓存中
    业务成功时响应数据是空的
    :param payment_type:
    :return:
    """
    # 接口基本信息
    url = f'http://www.mtxshop.com:7002/trade/checkout-params/payment-type'
    headers = {
        'Authorization': token
    }
    data = {
        'payment_type': payment_type
    }
    # 发起接口调用
    resp = session.request(method='post', url=url, data=data, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


def create_trade(client='PC', way='BUY_NOW'):
    """
    创建交易接口才是真正的下单接口，会根据不同的way来决定读取哪种redis缓存的订单信息，然后将其生成订单数据存入数据库
    :param client:
    :param way:
    :return:
    """
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
    return resp  # 返回响应对象，提供给调用方使用


def search_order(order_status='', page_no=1, page_size=5, key_words='沙陌', start_time=1657987200, end_time=1658505599):
    # 接口基本信息
    url = f'http://www.mtxshop.com:7002/trade/orders'
    headers = {
        'Authorization': token
    }
    params = {
        'order_status': order_status,
        'page_no': page_no,
        'page_size': page_size,
        'key_words': key_words,
        'start_time': start_time,
        'end_time': end_time

    }
    resp = session.request(method='get', url=url, params=params, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


def cancel_order(order_sn, reason='不想要了'):
    # 接口基本信息
    url = f'http://www.mtxshop.com:7002/trade/orders/{order_sn}/cancel'
    headers = {
        'Authorization': token
    }
    data = {
        'reason ': reason

    }
    resp = session.request(method='post', url=url, data=data, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


def confirm_rog(order_sn):
    """
    确认收货接口
    :param order_sn:
    :return:
    """
    # 接口基本信息
    url = f'http://www.mtxshop.com:7002/trade/orders/{order_sn}/rog'
    headers = {
        'Authorization': token
    }

    resp = session.request(method='post', url=url, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


def return_goods(order_sn, sku_id, region=2799):
    """
    申请退货接口
    :param order_sn:
    :param sku_id:
    :param region:
    :return:
    """
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
        'region': region,
    }

    resp = session.request(method='post', url=url, data=data, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


def comment(order_sn, sku_id, content='这是评论内容'):
    """
    提交评论接口
    :param order_sn:
    :param sku_id:
    :param content:
    :return:
    """
    # 接口基本信息
    url = f'http://www.mtxshop.com:7002/members/comments'
    headers = {
        'Authorization': token
    }
    json = {
        "comments": [
            {
                "content": content,
                "grade": "good",
                "images": [],
                "sku_id": sku_id
            }
        ],
        "delivery_score": 5,
        "description_score": 5,
        "order_sn": order_sn,
        "service_score": 5
    }

    resp = session.request(method='post', url=url, json=json, headers=headers)
    return resp  # 返回响应对象，提供给调用方使用


if __name__ == '__main__':
    resp = buyer_login()  # 先调用登录接口，会产生token
    print(f'响应结果是:{resp.text}')
    # resp = buy_now()
    # resp = add_cart()
    # resp = create_trade()
    # resp = set_paytype()
    resp = confirm_rog(order_sn='20220724000013')
    print(resp.status_code)
    print(f'响应结果是:{resp.text}')
    # 如果响应结果是空的，是不能使用resp.json()去获取的
    # print(resp.json())
