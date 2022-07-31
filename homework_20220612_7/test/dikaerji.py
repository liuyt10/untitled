# -*- coding:utf-8 -*-
import pytest
from classcode_07.apistudy.requests_study.mtxshop_apis import buy_now, delete_cart, add_cart, create_trade, buyer_login, \
    set_addressid


# @pytest.mark.usefixtures('get_buyer_token')
class TestCreateTrade:
    client_data = ['PC', 'WAP', 'NATIVE', 'REACT', 'MINI']
    way_data = ['BUY_NOW', 'CART']
    expect_statuscode = [200]

    # def setup_class(self):
    #     buyer_login()

    @pytest.mark.parametrize('client', client_data)
    @pytest.mark.parametrize('way', way_data)
    @pytest.mark.parametrize('expect_status_code', expect_statuscode)
    def test_create_trade(self, client, way, expect_status_code, get_buyer_token1):
        # 注意：创建交易的接口的订单数据来源是根据way的不同来调用不同的接口创造数据
        if way == 'BUY_NOW':
            buy_now()
            set_addressid()
        elif way == 'CART':
            delete_cart()
            add_cart()
        resp = create_trade(client=client, way=way)
        print(f'创建交易的结果是：{resp.text}')
        assert resp.status_code == expect_status_code


class TestAddCart:

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
