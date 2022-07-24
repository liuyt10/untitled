# -*- coding:utf-8 -*-
import requests

session = requests.session()
token = ''


def request_login(mobile, sms_code, uuid):  # 登录用户
    url = f'http://www.mtxshop.com:7002/passport/login/{mobile}'
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
    token = resp.json()['access_token']
    return resp


def checking_order(key_words='', order_status='', page_no=1, page_size=5):  # 查询订单
    url = r'http://www.mtxshop.com:7002/trade/orders'
    header = {
        'Authorization': token
    }
    data = {
        'key_words': key_words,
        'order_status': order_status,
        'page_no': page_no,
        'page_size': page_size
    }
    resp = session.request(method='get', headers=header, url=url, data=data)
    return resp


def cancel_order(order_sn, reason):  # 取消订单
    url = f'http://www.mtxshop.com:7002/trade/orders/{order_sn}/cancel'
    header = {
        'Authorization': token
    }
    data = {
        'order_sn': order_sn,
        'reason': reason
    }
    resp = session.request(method='post', url=url, headers=header, data=data)
    return f'会员创建的订单号{order_sn}已经被取消，取消原因是{reason}'


def order_rog(order_sn):  # 确认收货
    url = f'http://www.mtxshop.com:7002/trade/orders/{order_sn}/rog'
    header = {
        'Authorization': token
    }
    data = {
        'order_sn': order_sn
    }
    resp = session.request(method='post', url=url, headers=header, data=data)
    return f'会员的待确认收货订单{order_sn}，已经确认收货'


# def return_goods():  # 退货申请
#     url = 'http://www.mtxshop.com:7002/after-sales/apply/return/goods'
#     header = {
#         'Authorization': token
#     }
#     data = {
#         'order_sn': order_sn
#     }
#     resp = session.request(method='post', url=url, headers=header, data=data)
#     return resp


def submit_comments(sku_id, order_sn, content):  # 提交评论
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
    return resp


if __name__ == '__main__':
    res = request_login(mobile='13557047908', uuid='26224', sms_code='908908')  # 用户登录
    # print(token)
    # 调用查询会员全部订单函数,并返回该会员总的订单数量
    check_or = checking_order().json()
    print(check_or)
    print(f"会员拥有的总的订单数是：{check_or['data_total']}")
    print('******************************************************')

    # 获取会员最新订单的订单号,然后调用取消订单接口，取消该订单
    order_id = check_or['data'][0]['order_id']
    print(f'会员最新创建的订单号是：{order_id}')
    candel_or = cancel_order(order_id, '测试代码')  #
    print(candel_or)
    print('******************************************************')

    # 调用查询会员全部待确认收货的订单，获取用户最新创建的确认收货订单的订单号，然后调用确认收货接口
    check_or = checking_order(order_status='WAIT_ROG').json()
    order_id = check_or['data'][0]['order_id']
    print(f'会员最新待确认收货的订单号是：{order_id}')
    rog_or = order_rog(order_id, )  #
    print(rog_or)

    # 调用查询会员全部待确认收货的订单，获取用户最新创建的确认收货订单的订单号，然后调用确认收货接口
    check_or = checking_order(order_status='WAIT_COMMIT').json()
    sku_id = check_or['data'][0]['sku_list'][0]['sku_id']  # 获取到商品编号
    print(f'会员最新待评论的订单号是：{sku_id}')
    order_sn = check_or['data'][0]['trade_sn']  # 获取到订单号
    rog_or = submit_comments(sku_id, order_sn, '此参数为传入的评价内容')
    print(rog_or.json())
