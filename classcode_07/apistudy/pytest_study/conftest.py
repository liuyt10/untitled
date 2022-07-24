# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : conftest.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-24 11:27
# @Copyright: 北京码同学

# 解决pycharm上执行pytest后看到的用例标题中文乱码
from typing import List

import pytest

from classcode_07.apistudy.redis_study.redis_connect import RedisUtil
from classcode_07.apistudy.requests_study.mtxshop_apis import buyer_login, buy_now, create_trade


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


"""
scope表示该fixture的作用域
session:表示在本次pytest执行时，只会被执行一次
module:表示在每个模块执行时，只会被执行一次
class:表示在每个测试类执行时，只会被执行一次
function:表示在每个测试用例执行时，都会被执行
package:和session基本上差不多
"""
"""
autouse表示该fixture函数是否被自动调用，默认是False
设置为True那么会根据作用域自动完成调用
设置为False则需要手动完成调用
手动调用分为两种：
1.@pytest.mark.usefixtures('get_buyer_token') # 括号里就是fixture函数的名称
2.在测试用例函数参数中直接写上fixture函数的名称
"""


# @pytest.fixture(scope='function',autouse=True)
# def get_buyer_token():
#     buyer_login()
#     print('获取买家登录的token')
@pytest.fixture(scope='session', autouse=True)
def get_buyer_token():
    resp = buyer_login()
    uid = resp.json()['uid']  # 获取用户id
    print('获取买家登录的token')
    yield uid  # 从yield下一行开始，表示的是后置动作
    print('这是后置动作')


# 使用fixture初始化一些数据，将得到的数据返回，提供给测试用例使用
@pytest.fixture(scope='function')
def get_order_sn():
    buy_now()
    resp = create_trade()
    order_sn = resp.json()['order_list'][0]['sn']
    return order_sn


# 比如 前置动作创建一个商品，得到商品id及sku_id给需要的接口使用
# 用完之后将该商品再清除掉
@pytest.fixture(scope='function')
def goods_data():
    print('创建一个商品')  # 前置动作
    yield '返回商品id'  # 返回数据
    print('清除商品')  # 后置动作


@pytest.fixture(scope='session', autouse=True)
def get_redis():
    redis_util = RedisUtil(host='121.42.15.146', pwd='testfan')
    yield redis_util
