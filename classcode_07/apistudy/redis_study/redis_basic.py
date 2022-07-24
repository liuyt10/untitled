# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : redis_basic.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-24 15:37
# @Copyright: 北京码同学
import redis

# 先创建一个连接池
pool = redis.ConnectionPool(host='localhost',port=6379,decode_responses=True,db=0)
r = redis.Redis(connection_pool=pool) # 从连接池里拿到一个连接对象
# 通过连接对象，对redis进行操作

# 操作字符串
r.set('gender','male',ex=30)
r.get('gender')

# 操作哈希
r.hset('userinfo','name','shamo')
r.hset('userinfo','age',18)
print(r.hgetall('userinfo'))

# 操作列表
r.lpush('listlist','1111','222','333')
print(r.lrange('listlist',0,-1))

# 操作集合
r.sadd('setset','data1','data1','data2')
print(r.smembers('setset'))

# 操作有序集合
r.zadd('youxuset',{'data1':6,'data2':3,'data3':4})
print(r.zrange('youxuset',0,-1,desc=True))

# 获取某些数据对应的类型
print(r.type('youxuset'))
print(r.type('setset'))
print(r.type('listlist'))
print(r.type('userinfo'))
print(r.type('gender'))