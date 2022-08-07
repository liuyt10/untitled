# -*- coding:utf-8 -*-
from api.base_api import BaseBuyerApi


class SetAddressId(BaseBuyerApi):  # 设置支付地址
    def __init__(self, address_id=6304):
        super().__init__()
        self.url = f'{self.host}/trade/checkout-params/address-id/{address_id}'
        self.method = 'post'


class SetPayType(BaseBuyerApi):  # 设置支付地址
    def __init__(self, payment_type='COD'):
        super().__init__()
        self.url = f'{self.host}/trade/checkout-params/payment-type'
        self.method = 'post'
        self.data = {
            'payment_type': payment_type
        }
