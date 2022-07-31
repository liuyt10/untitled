# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_003_checkout_params_api.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 16:54
# @Copyright: 北京码同学
import javaobj
import pytest

from api.base_api import BaseBuyerApi
from api.buyer.checkout_params_apis import SetAddressIdApi


class TestSetAddressIdApi:


    def test_setAddressid(self,redis_util):
        resp = SetAddressIdApi(address_id=6338).send()
        assert resp.status_code == 200
        # redis数据断言
        res = redis_util.get(f'{{CHECKOUT_PARAM_ID_PREFIX}}_{BaseBuyerApi.uid}')  # 59是用户id
        # print(res)
        # res在redis里是个hash，对应的就是python里的字典，所以我们直接遍历他
        for key, value in res.items():
            # 将key转换
            key1 = javaobj.loads(key)
            # print(key1)
            # print(value)
            try:
                value1 = javaobj.loads(value)
                print(value1)
            except:
                pass
            if key1 == 'addressId':
                # print(value1)
                pytest.assume(value1==6338,f'实际值是:{value1},期望值是：6338')
            # elif key1 == 'paymentType':
            #     # 因为对应的value是个对象，
            #     print(dir(value1))
            #     print(value1.__getattribute__('constant'))