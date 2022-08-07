# -*- coding:utf-8 -*-
import pytest

from api.buyer.cart_api import BuyNowApi, DelectableApi, AddCartApi
from api.buyer.checkout_params_api import SetAddressId
from api.buyer.order_api import CreatTradeApi


class TestCreatTradeApi:
    client_data = ['PC', 'WAP', 'NATIVE', 'REACT', 'MINI']
    way_data = ['BUY_NOW', 'CART']
    expect_statuscode = [200]

    # def setup_class(self):
    #     buyer_login()

    @pytest.mark.parametrize('client', client_data)
    @pytest.mark.parametrize('way', way_data)
    @pytest.mark.parametrize('expect_status_code', expect_statuscode)
    def test_create_trade(self, client, way, expect_status_code):
        # 注意：创建交易的接口的订单数据来源是根据way的不同来调用不同的接口创造数据
        if way == 'BUY_NOW':
            BuyNowApi().send()
            SetAddressId().send()
        elif way == 'CART':
            DelectableApi().send()  # 清空购物车，防止垃圾数据造成失败
            AddCartApi(sku_id=17418).send()
        create_trade_api = CreatTradeApi(client=client, way=way)
        resp = create_trade_api.send()
        print(f'创建交易的结果是：{resp.text}')
        assert resp.status_code == expect_status_code
