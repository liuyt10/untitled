# -*- coding:utf-8 -*-

import pymysql

connect = pymysql.Connect(
    host='121.42.15.146',
    port=3306,
    user='root',
    password='Testfan#123',
    charset='utf8md5',
    cuersorclass=pymysql.cursors.DictCursor
)

cursor = connect.cursor()
