# -*- coding:utf-8 -*-
import pymysql


class DBUtil:  # 创建一个数据库
    def __init__(self, host, user, password, port=3306):
        self.connect = pymysql.Connect(  # 创建一个数据库的连接对象
            host=host,
            user=user,
            port=port,
            password=password,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # 操作游标返回数据类型为字典类型
        )

    def select(self, sql):  # 查询SQL语句，得出结果
        cursor = self.connect.cursor()  # 数据库的对象调用cursor()，获取到一个游标对象
        cursor.execute(sql)  # 游标对象执行SQL语句
        data = cursor.fetchall()
        self.connect.commit()  # 提交事务，如果不提交下次查询，查不到新数据,也可以在更新操作处增加提交事务，但是所有更改事务都需要增加提交事务，
        # 不如查询操作增加一个提交事务更方便
        cursor.close()
        return data

    def upedata(self, sql):  # 更新
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()  # 提交事务，力求数据库都更新到最新
        cursor.close()

    def close(self):  # 关闭数据库
        if self.connect != None:
            self.connect.close()


if __name__ == '__main__':
    db_util = DBUtil(host='121.42.15.146', user='root', password='Testfan#123')  # 数据库的对象
    res = db_util.select('select * from mtxshop_trade.es_order order by order_id desc limit 2')
    print(res)
