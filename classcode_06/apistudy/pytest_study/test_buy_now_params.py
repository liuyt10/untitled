# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_buy_now_params.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-24 10:30
# @Copyright: 北京码同学

"""
sku_id不存在
sku_id已下架
sku_id已删除
num为0
num为-1
num超过库存
"""
import pytest

from requests_study.mtxshop_apis import buy_now, buyer_login

test_data = [
    ['sku_id不存在',83774663,    1,      500,'004','不合法'],
    ['sku_id已下架',538     ,    1,      500,'004','不合法'],
    ['sku_id已删除',18575     ,  1,      500,'004','不合法'],
    ['num为0',     17418,       0,      400,'004','购买数量必须大于0'],
    ['num为-1',    17418,       -1,     400,'004','购买数量必须大于0'],
    ['num超过库存', 17418,  99999999,    500,'451','商品库存已不足，不能购买。'],
]
# def setup_module():
#     buyer_login()
@pytest.mark.parametrize('casename,sku_id,num,expect_statuscode,expect_code,expect_message',test_data)
def test_buy_now_params(casename,sku_id,num,expect_statuscode,expect_code,expect_message):

    resp = buy_now(sku_id=sku_id,num=num)
    print(resp.status_code)
    status_code = resp.status_code
    print(resp.text)
    assert status_code==expect_statuscode
    print(resp.text)
    # 断言响应信息中的code
    assert resp.json()['code'] == expect_code
    assert resp.json()['message'] == expect_message