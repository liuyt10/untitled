# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : db_basic.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 9:52
# @Copyright: 北京码同学
import time

import pymysql

# 创建数据库连接对象，需要数据库的基本信息
connect = pymysql.Connect(
    host='121.42.15.146',
    port=3306,
    user='root',
    password='Testfan#123',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor # 这个参数指的是操作的结果是一个字典类型
)
# 得到一个游标对象，使用游标对象做数据库的基本操作
cursor = connect.cursor() # 这个游标会将当前数据库的结果集存储起来，后续的游标操作都是在这个结果集上操作的
# 查询订单表的订单，按照order_id倒序排列，取最上面的两行
# time.sleep(30)
cursor.execute('select * from mtxshop_trade.es_order order by order_id desc limit 2')
# 得到查询的所有结果
res = cursor.fetchall()
print(res) #这是一个列表套字典的结构，一个字典就表示查到的一行数据
print(type(res))
# 得到第一行数据的order_status
print(res[0]['order_status'])
cursor.close()
connect.close()
