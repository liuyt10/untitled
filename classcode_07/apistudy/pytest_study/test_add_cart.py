# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_add_cart.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 16:38
# @Copyright: 北京码同学


# 以类的形式编写测试用例
from classcode_07.apistudy.requests_study.mtxshop_apis import buyer_login, add_cart


class TestAddCart:

    # 当前类下所有的测试用例执行前调用登录接口
    def setup_class(self):
        buyer_login()
        print('当前类下所有的测试用例执行前调用登录接口')
    def teardown_class(self):
        print('当前类下所有的测试用例执行后执行的动作')

    def setup_method(self):
        print('在当前类下每条测试用例执行前去执行')
    def teardown_method(self):
        print('在当前类下每条测试用例执行后去执行')

    def test_add_cart1(self):
        resp = add_cart(sku_id=83774663)
        print(resp.status_code)
        status_code = resp.status_code
        assert status_code == 500
        print(resp.text)
        # 断言响应信息中的code
        assert resp.json()['code'] == '451'
        assert resp.json()['message'] == '商品已失效，请刷新购物车'
    def test_add_cart2(self):
        resp = add_cart(sku_id=538)
        print(resp.status_code)
        status_code = resp.status_code
        assert status_code == 500
        print(resp.text)
        # 断言响应信息中的code
        assert resp.json()['code'] == '451'
        assert resp.json()['message'] == '商品已失效，请刷新购物车'