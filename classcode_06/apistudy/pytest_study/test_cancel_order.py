# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_cancel_order.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-24 11:51
# @Copyright: 北京码同学
from requests_study.mtxshop_apis import cancel_order


class TestCancelOrder:


    def test_cacel_order(self,get_order_sn):
        resp = cancel_order(order_sn=get_order_sn)
        assert resp.status_code == 200