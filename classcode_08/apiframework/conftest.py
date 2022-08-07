# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : conftest.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 11:33
# @Copyright: 北京码同学
from typing import List

import pytest

from classcode_08.apiframework.api.base_api import BaseBuyerApi
from classcode_08.apiframework.api.buyer.buyer_login_apis import BuyerLoginApi
from classcode_08.apiframework.common.db_util import DBUtil
from classcode_08.apiframework.common.redis_util import RedisUtil


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

# 自定义一个fixture，来实现买家token的提取和赋值
@pytest.fixture(scope='session',autouse=True)
def get_buyer_token():
    buyer_login_api = BuyerLoginApi()
    resp = buyer_login_api.send()
    BaseBuyerApi.buyer_token = resp.json()['access_token']
    BaseBuyerApi.uid = resp.json()['uid']

@pytest.fixture(scope='session',autouse=True)
def redis_util():
    redis_util = RedisUtil(host='121.42.15.146', pwd='testfan')
    yield redis_util

@pytest.fixture(scope='session',autouse=True)
def db_util():
    db_util = DBUtil(host='121.42.15.146',user='root',password='Testfan#123')
    yield db_util
    db_util.close()
