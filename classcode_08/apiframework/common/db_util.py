# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : db_util.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 10:26
# @Copyright: 北京码同学
import time

import pymysql


class DBUtil:

    def __init__(self,host,user,password,port=3306):
        self.connect = pymysql.Connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        self.connect.commit()# 提交事务，如果不提交下次查询，查不到新数据
        cursor.close()
        return data
    def update(self,sql):
        """
        insert、update、delete
        :param sql:
        :return:
        """
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()
    def close(self):
        if self.connect!=None:
            self.connect.close()
if __name__ == '__main__':
    db_util = DBUtil(host='121.42.15.146',user='root',password='Testfan#123')
    for i in range(5):
        time.sleep(10)
        res = db_util.select('select * from mtxshop_trade.es_order order by order_id desc limit 2')
        print(res)
    db_util.close()