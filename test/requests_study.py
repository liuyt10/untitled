# -*- coding:utf-8 -*-
import requests
import pytest

url = 'http://www.mtxshop.com:7000/pages/article-categories'
params = {
    'category_type': 'HELP'
}

resp = requests.get(url=url, params=params)
print(resp.status_code)
print(resp.text)
print(resp.json())

session = requests.session()
res = session.request(method='get', url=url, params=params)
