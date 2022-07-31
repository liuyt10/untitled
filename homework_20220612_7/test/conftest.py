# -*- coding:utf-8 -*-
from typing import List

import pytest
from classcode_07.apistudy.requests_study.mtxshop_apis import buyer_login, buy_now, create_trade


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:  # 钩子函数
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


# @pytest.fixture(scope='class', autouse=True)
# def get_buyer_token1():
#     buyer_login()
#     print('执行买家登录，获取token')


@pytest.fixture(scope='function')
def get_order_sn1():
    buy_now()
    resp = create_trade()
    order_sn = resp.json()['order_list'][0]['sn']
    return order_sn


@pytest.fixture(scope='session', autouse=True)
def get_buyer_token():
    buyer_login()
    # print('获取买家登录的Token')
    # yield  # 从yield下一行开始，表示后置动作
    # print('这是后置动作')


@pytest.fixture(scope='function')
def goods_data1():
    print('创建一个商品')
    yield '返回商品id'
    print('清除商品')
