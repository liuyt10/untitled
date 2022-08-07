# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_create_trade_params_dikaerji.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-24 10:53
# @Copyright: 北京码同学
import time

import pytest

# @pytest.mark.usefixtures('get_buyer_token')
from classcode_08.requests_study.mtxshop_apis import buy_now, delete_cart, add_cart, create_trade


class TestCreateTrade:
    client_data = ['PC', 'WAP', 'NATIVE', 'REACT', 'MINI']  # 5
    way_data = ['BUY_NOW', 'CART']  # 2
    expect_statuscode = [200]  # 1

    # 生成用例的总数 5*2*1=10
    # def setup_class(self):
    #     buyer_login()

    @pytest.mark.parametrize('client', client_data)
    @pytest.mark.parametrize('way', way_data)
    @pytest.mark.parametrize('expect_status_code', expect_statuscode)
    def test_create_trade(self, client, way, expect_status_code, get_buyer_token, get_db):
        # 注意：创建交易的接口的订单数据来源是根据way的不同来调用不同的接口创造数据
        # 如果way是BUY_NOW，那么需要先调用立即购买接口
        # 如果way是CART，那么需要先调用添加购物车接口
        if way == 'BUY_NOW':
            buy_now()
        elif way == 'CART':
            delete_cart()  # 清空购物车，防止垃圾数据造成失败
            add_cart()
        resp = create_trade(client=client, way=way)
        print(f'创建交易结果是:{resp.text}')
        assert resp.status_code == expect_status_code
        # 集成数据库断言
        # 创建交易的接口，本身会往订单表中存入一条数据
        # 怎么做断言？
        # 从响应信息中提取订单编号，然后去查库，如果能查到数据，说明数据存入正确
        resp_sn = resp.json()['order_list'][0]['sn']
        # db_util = DBUtil(host='121.42.15.146', user='root', password='Testfan#123')
        res = get_db.select(f'select * from mtxshop_trade.es_order where trade_sn={resp_sn}')
        # res是个列表套字典
        assert len(res) == 1
        # 判断核心字段对不对
        # 订单状态初始时是NEW,定时任务会自动将其变成CONFIRM,因为我们用的货到付款
        # 由于咱们项目本身比较慢，所以要判断得在这里加个等待
        time.sleep(1)
        pytest.assume(res[0]['order_status'] == 'CONFIRM', f'实际值是:{res[0]["order_status"]}')
        # db_util.close()


# 以类的形式编写测试用例
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
