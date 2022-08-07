# -*- coding:utf-8 -*-
import pytest

from api.buyer.cart_api import BuyNowApi
from comment.file_load import read_excel


class TestBuyNowApi:
    # test_data = [
    #     ['sku_id不存在', 83774663, 1, 500, '004', '不合法'],
    #     ['sku_id已下架', 538, 1, 200, '004', '不合法'],
    #     ['sku_id已删除', 18575, 1, 500, '004', '不合法'],
    #     ['num为0', 17418, 0, 400, '004', '购买数量必须大于0'],
    #     ['num为-1', 17418, -1, 400, '004', '购买数量必须大于0'],
    #     ['num超过库存', 17418, 99999999, 500, '451', '商品库存已不足，不能购买。'],
    # ]
    test_data = read_excel(f'\data\mtxshop_testdata.xlsx', '立即购买数据')

    @pytest.mark.parametrize('casename,sku_id,num,expect_statuscode,expect_code,expect_message', test_data)
    def test_buy_now_params(self, casename, sku_id, num, expect_statuscode, expect_code, expect_message):
        # 调用BuyNowApi
        buy_now_api = BuyNowApi(sku_id, num)
        resp = buy_now_api.send()
        status_code = resp.status_code
        print(resp.text)
        pytest.assume(status_code == expect_statuscode, f'实际值是:{status_code},期望值是：{expect_statuscode}')
        pytest.assume(resp.json()['code'] == expect_code.replace('"', ''),
                      f"实际值是：{resp.json()['code']},期望值是：{expect_code}")
        pytest.assume(resp.json()['message'] == expect_message, f"实际值是：{resp.json()['message']},期望值是：{expect_message}")
