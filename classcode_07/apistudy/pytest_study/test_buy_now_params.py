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
import javaobj
import pytest

from redis_study.redis_connect import RedisUtil
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
    # assert status_code==expect_statuscode
    pytest.assume(status_code==expect_statuscode,f'实际值是:{status_code},期望值是：{expect_statuscode}')
    print(resp.text)
    # 断言响应信息中的code
    # assert resp.json()['code'] == expect_code
    # assert resp.json()['message'] == expect_message
    # 第一个参数是判断表达式，第二个参数是失败之后的提示语
    pytest.assume(resp.json()['code'] == expect_code,f"实际值是：{resp.json()['code']},期望值是：{expect_code}")
    pytest.assume(resp.json()['message'] == expect_message,f"实际值是：{resp.json()['message']},期望值是：{expect_message}")
def test_buy_now(get_redis,get_buyer_token):

    resp = buy_now(sku_id=9257,num=1)
    print(resp.status_code)
    status_code = resp.status_code
    print(resp.text)
    # assert status_code==expect_statuscode
    pytest.assume(status_code==200,f'实际值是:{status_code},期望值是：200')
    print(resp.text)
    # 成功后，响应信息是空
    # 那么我要针对该接口存储在redis中的数据进行判断
    # redis_util = RedisUtil(host='121.42.15.146',pwd='testfan')
    res = get_redis.get(f'{{BUY_NOW_ORIGIN_DATA_PREFIX}}_{get_buyer_token}') #59是用户id
    res_obejct = javaobj.loads(res)
    # 获取立即购买时存储到redis的num数量
    expect_num = res_obejct[0].__getattribute__('num')
    expect_skuid = res_obejct[0].__getattribute__('skuId')
    pytest.assume(expect_num==1,f'实际值是:{expect_num},期望值是：1')
    pytest.assume(expect_skuid == 9257, f'实际值是:{expect_skuid},期望值是：9257')

