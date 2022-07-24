# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_buyer_login.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-17 15:43
# @Copyright: 北京码同学
from classcode_07.apistudy.requests_study.mtxshop_apis import buyer_login


def test_buyer_login():
    # 调用登录接口，传入测试数据，拿到响应结果
    resp = buyer_login(username='shamo',password='e10adc3949ba59abbe56e057f20f883e')
    # 针对响应结果做判断，这个过程就叫做断言
    # 断言响应状态码
    status_code = resp.status_code
    assert status_code == 200
    # 断言响应信息
    resp_username = resp.json()['username']
    assert resp_username == 'shamo'