# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_buy_now.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 16:15
# @Copyright: 北京码同学

"""
sku_id不存在
sku_id已下架
sku_id已删除
num为0
num为-1
num超过库存
"""
from requests_study.mtxshop_apis import buyer_login, buy_now


# 在当前模块下所有用例执行前去调用登录接口
def setup_module():
    buyer_login()
    print('在当前模块下所有用例执行前去调用登录接口')
def teardown_module():
    print('在当前模块下所有用例执行后要做的后置动作')

def setup_function():
    print('每条测试用例执行前都会执行')
def teardown_function():
    print('每条测试用例执行后都会执行')
# sku_id不存在
def test_buy_now1():
    # buyer_login()
    resp = buy_now(sku_id=83774663)
    print(resp.status_code)
    status_code = resp.status_code
    assert status_code==500
    print(resp.text)
    # 断言响应信息中的code
    assert resp.json()['code'] == '004'
    assert resp.json()['message'] == '不合法'
# sku_id已下架
def test_buy_now2():
    # buyer_login()
    resp = buy_now(sku_id=538)
    print(resp.status_code)
    status_code = resp.status_code
    assert status_code==500
    print(resp.text)
    # 断言响应信息中的code
    assert resp.json()['code'] == '004'
    assert resp.json()['message'] == '不合法'