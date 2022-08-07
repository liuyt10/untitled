# -*- coding:utf-8 -*-
from comment.client import RequestClient


class BuyerLoginApi(RequestClient):
    # 初始化函数是用来定义接口的所有默认信息的
    def __init__(self):
        super().__init__()
        self.url = f'http://www.mtxshop.com:7002/passport/login/13557047908'
        self.method = 'post'
        self.data = {
            'mobile': 13557047908,
            'sms_code': 908908,
            'uuid': 123456
        }


if __name__ == '__main__':
    buyer_login_api = BuyerLoginApi()
    print(buyer_login_api.method)
    # print(buyer_login.json()['mobile'])
    resp = buyer_login_api.send()
    print(resp.json())
    print(BuyerLoginApi().send().json()['access_token'])
