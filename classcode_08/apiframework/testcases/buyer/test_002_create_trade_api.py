# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_002_create_trade_api.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 15:29
# @Copyright: 北京码同学
import time

import pytest

from classcode_08.apiframework.common.file_load import load_yaml_file


class TestCreateTradeApi:
    yaml_data = load_yaml_file('/data/mtxshop_testdata.yml')['创建交易']
    client_data = yaml_data['client'] # 5
    way_data = yaml_data['way'] # 2
    expect_statuscode = yaml_data['expect_statuscode'] # 1
    # 生成用例的总数 5*2*1=10
    # def setup_class(self):
    #     buyer_login()

    @pytest.mark.parametrize('client',client_data)
    @pytest.mark.parametrize('way',way_data)
    @pytest.mark.parametrize('expect_status_code',expect_statuscode)
    def test_create_trade(self,client,way,expect_status_code,db_util):
        # 注意：创建交易的接口的订单数据来源是根据way的不同来调用不同的接口创造数据
        # 如果way是BUY_NOW，那么需要先调用立即购买接口
        # 如果way是CART，那么需要先调用添加购物车接口
        if way=='BUY_NOW':
            BuyNowApi(sku_id=17418).send()
        elif way == 'CART':
            DeleteCartApi().send()# 清空购物车，防止垃圾数据造成失败
            AddCartApi(sku_id=17418).send()
        create_trade_api = CreateTradeApi(client=client,way=way)
        resp = create_trade_api.send()
        print(f'创建交易结果是:{resp.text}')
        assert resp.status_code == expect_status_code

        # 数据库断言
        resp_sn = resp.json()['order_list'][0]['sn']
        # db_util = DBUtil(host='121.42.15.146', user='root', password='Testfan#123')
        res = db_util.select(f'select * from mtxshop_trade.es_order where trade_sn={resp_sn}')
        # res是个列表套字典
        assert len(res) == 1
        time.sleep(1)
        pytest.assume(res[0]['order_status'] == 'CONFIRM',f'实际值是:{res[0]["order_status"]}')
