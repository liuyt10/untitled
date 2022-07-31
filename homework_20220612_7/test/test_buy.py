# -*- coding:utf-8 -*-
import pytest
from classcode_07.apistudy.requests_study.mtxshop_apis import buy_now, buyer_login

test_data = [
    ['sku_id不存在', 83774663, 1, 500, '004', '不合法'],
    ['sku_id已下架', 538, 1, 500, '004', '不合法'],
    ['sku_id已删除', 18575, 1, 500, '004', '不合法'],
    ['num为0', 17418, 0, 400, '004', '购买数量必须大于0'],
    ['num为-1', 17418, -1, 400, '004', '购买数量必须大于0'],
    ['num超过库存', 17418, 99999999, 500, '452', '商品库存已不足1，不能购买。']
]


# def setup_module():
#     buyer_login()


@pytest.mark.parametrize('casename,sku_id,num,expect_statuscode,expect_code,expect_message', test_data)
def test_buy_now_params(casename, sku_id, num, expect_statuscode, expect_code, expect_message):
    resp = buy_now(sku_id=sku_id, num=num)
    print(resp.status_code)
    print(resp.text)
    assert resp.status_code == expect_statuscode,'响应码不一致'
    # pytest.assume(resp.status_code == expect_statuscode, f'实际值是:{resp.status_code},期望值是：{expect_statuscode}')

    pytest.assume(resp.json()['code'] == expect_code,
                  f"实际值是************：{resp.json()['code']},期待值是**********：{expect_code}")
    pytest.assume(resp.json()['message'] == expect_message,
                  f"实际值是**********：{resp.json()['message']},期待值是*********：{expect_message}")
