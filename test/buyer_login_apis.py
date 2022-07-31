# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : buyer_login_apis.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 11:51
# @Copyright: 北京码同学
from test.client import RequestsClient


class BuyerLoginApi(RequestsClient):
    # 初始化函数是用来定义接口的所有默认信息的
    def __init__(self):
        super().__init__()
        self.url = 'http://www.mtxshop.com:7002/passport/login'
        self.method = 'post'
        self.data = {
            'username': 'shamo',
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'captcha': '1512',
            'uuid': 'sdhhjshjdhdhd'
        }

if __name__ == '__main__':
    buyer_login_api = BuyerLoginApi()
    # resp = buyer_login_api.send(method=buyer_login_api.method,url=buyer_login_api.url,data=buyer_login_api.data)
    resp = buyer_login_api.send()
    print(resp.json())