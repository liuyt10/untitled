# -*- coding:utf-8 -*-
from typing import List

import pytest

from api.base_api import BaseBuyerApi
from api.buyer.buyer_login_api import BuyerLoginApi
from api.manager.manager_login_api import ManagerLoginApi
from api.seller.seller_login_api import SellerLoginApi


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


# 自定义一个fixture，来实现买家Token的提取和赋值
@pytest.fixture(scope='session', autouse=True)
def get_buyer_token():
    buyer_login_api = BuyerLoginApi()
    resp = buyer_login_api.send()
    BaseBuyerApi.buyer_token = resp.json()['access_token']


@pytest.fixture(scope='session', autouse=True)
def get_seller_token():
    seller_login_api = SellerLoginApi()
    resp = seller_login_api.send()
    SellerLoginApi.seller_token = resp.json()['access_token']


@pytest.fixture(scope='session', autouse=True)
def get_manager_token():
    manager_login_api = ManagerLoginApi()
    resp = manager_login_api.send()
    ManagerLoginApi.manager_token = resp.json()['access_token']
