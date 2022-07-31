# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_001_buy_now_api.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 14:21
# @Copyright: 北京码同学
import javaobj
import pytest

from api.base_api import BaseBuyerApi
from api.buyer.cart_apis import BuyNowApi
from common.file_load import read_excel


class TestBuyNowApi:

    # def setup_class(self):
    #     pass
    # test_data = [
    #     ['sku_id不存在', 83774663, 1, 500, '004', '不合法'],
    #     ['sku_id已下架', 538, 1, 500, '004', '不合法'],
    #     ['sku_id已删除', 18575, 1, 500, '004', '不合法'],
    #     ['num为0', 17418, 0, 400, '004', '购买数量必须大于0'],
    #     ['num为-1', 17418, -1, 400, '004', '购买数量必须大于0'],
    #     ['num超过库存', 17418, 99999999, 500, '451', '商品库存已不足，不能购买。'],
    # ]
    test_data = read_excel('/data/mtxshop_testdata.xlsx', '立即购买数据')

    @pytest.mark.parametrize('casename,sku_id,num,expect_statuscode,expect_code,expect_message', test_data)
    def test_buy_now_params(self,casename, sku_id, num, expect_statuscode, expect_code, expect_message):
        # 调用BuyNowApi
        buy_now_api = BuyNowApi(sku_id=sku_id,num=num)
        resp = buy_now_api.send()
        status_code = resp.status_code
        print(resp.text)
        # assert status_code==expect_statuscode
        pytest.assume(status_code == expect_statuscode, f'实际值是:{status_code},期望值是：{expect_statuscode}')
        print(resp.text)
        # 第一个参数是判断表达式，第二个参数是失败之后的提示语
        pytest.assume(resp.json()['code'] == expect_code.replace('"',''), f"实际值是：{resp.json()['code']},期望值是：{expect_code}")
        pytest.assume(resp.json()['message'] == expect_message, f"实际值是：{resp.json()['message']},期望值是：{expect_message}")

    def test_buy_now_success(self,redis_util):
        buy_now_api = BuyNowApi(sku_id=17418)
        resp = buy_now_api.send()
        assert resp.status_code == 200
        # redis数据校验
        res = redis_util.get(f'{{BUY_NOW_ORIGIN_DATA_PREFIX}}_{BaseBuyerApi.uid}')  # 59是用户id
        res_obejct = javaobj.loads(res)
        # 获取立即购买时存储到redis的num数量
        expect_num = res_obejct[0].__getattribute__('num')
        expect_skuid = res_obejct[0].__getattribute__('skuId')
        pytest.assume(expect_num == 1, f'实际值是:{expect_num},期望值是：1')
        pytest.assume(expect_skuid == 17418, f'实际值是:{expect_skuid},期望值是：17418')

