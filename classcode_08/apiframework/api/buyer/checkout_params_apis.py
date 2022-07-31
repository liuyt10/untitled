# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : checkout_params_apis.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 13:59
# @Copyright: 北京码同学
from api.base_api import BaseBuyerApi


class SetAddressIdApi(BaseBuyerApi):

    def __init__(self,address_id):
        super().__init__()
        self.url = f'{self.host}/trade/checkout-params/address-id/{address_id}'
        self.method = 'post'
class SetPayTypeApi(BaseBuyerApi):

    def __init__(self,payment_type='COD'):
        super().__init__()
        self.url = f'{self.host}/trade/checkout-params/payment-type'
        self.method = 'post'
        self.data = {
            'payment_type':payment_type
        }