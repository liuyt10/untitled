# -*- coding:utf-8 -*-

import pymysql

connect = pymysql.Connect(
    cuersorclass=pymysql.cursors.DictCursor,  # 这个参数指的是操作的结果是一个字典类型
    host='121.42.15.146',
    port=3306,
    user='root',
    password='Testfan#123',
    charset='utf8md5'
)
'{CHECKOUT_PARAM_ID_PREFIX}_26224'
cursor = connect.cursor()
