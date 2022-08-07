# -*- coding:utf-8 -*-
from comment.client import RequestClient


class ManagerLoginApi(RequestClient):
    # 初始化函数是用来定义接口的所有默认信息的
    def __init__(self):
        super().__init__()
        self.url = f'http://www.mtxshop.com:7004/admin/systems/admin-users/login'
        self.method = 'get'
        self.params = {
            'username': 'admin',
            'password': '96e79218965eb72c92a549dd5a330112',
            'captcha': 1512,
            'uuid': '4c724bd0-140e-11ed-9e7d-1776d0dff6b6'
        }
