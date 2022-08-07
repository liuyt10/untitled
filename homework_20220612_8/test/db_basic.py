# -*- coding:utf-8 -*-

import pymysql

# 创建数据库连接对象，需要数据库的基本信息
connect = pymysql.Connect(
    host='121.42.15.146',  # 数据库ip地址
    port=3306,  # 数据库的端口号
    user='root',  # 数据库的用户名
    password='Testfan#123',  # 数据库的密码
    charset='utf8mb4',    # 数据库的编码
    cursorclass=pymysql.cursors.DictCursor  # 这个参数指的是操作的结果是一个字典类型，pymysql.cursors表示数据库的游标，dictcursor返回字典类型数据

)
# 数据库调用游标函数，通过连接对象，生成一个游标对象
cursor = connect.cursor()
# 通过游标对象调用execute执行函数，执行SQL语句，从mtxshop_trade库中的订单表es_order，按照order_id倒序排，取上面两个
cursor.execute('select * from mtxshop_trade.es_order order by order_id desc limit 2')
# 游标对象调用fetchall获取所有数据
res= cursor.fetchall()
print(res)
print(type(res))
# print(res[0]['order_id'])
cursor.close()
connect.close()
