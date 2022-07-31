# -*- coding:utf-8 -*-
from classcode_07.apistudy.requests_study.mtxshop_apis import cancel_order


class TestCancel:
    def test_cancel_order(self,get_order_sn1):
        resp= cancel_order(order_sn=get_order_sn1)
        print('***************'+get_order_sn1)
        assert resp.status_code == 200

