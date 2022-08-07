# -*- coding:utf-8 -*-
from api.base_api import BaseManagerApi
from api.manager.manager_login_api import ManagerLoginApi


class ApprovedProducts(BaseManagerApi):
    def __init__(self, goods_ids, result):
        super().__init__()
        self.url = f'{self.host}/admin/goods/batch/audit'
        self.method = 'post'
        self.json = {
            "goods_ids": [
                goods_ids
            ],
            "message": "string",
            "pass": result
        }


if __name__ == '__main__':
    manager_login_api = ManagerLoginApi()
    resp = manager_login_api.send()
    BaseManagerApi.manager_token = resp.json()['access_token']
    approved_product = ApprovedProducts(19122, 1)
    resp = approved_product.send()
    print(resp.status_code)
