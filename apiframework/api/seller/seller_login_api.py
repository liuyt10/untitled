# -*- coding:utf-8 -*-


from comment.client import RequestClient
from comment.encry_decry import md5


class SellerLoginApi(RequestClient):
    # 初始化函数是用来定义接口的所有默认信息的
    def __init__(self, username='shamoseller', password='123456'):
        super().__init__()
        self.url = f'http://www.mtxshop.com:7002/passport/login'
        self.method = 'post'
        self.data = {
            'username': username,
            'password': md5(password),
            'captcha': 1512,
            'uuid': '456781'
        }

if __name__ == '__main__':
    res = SellerLoginApi().send()
    print(res.json())
