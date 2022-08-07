# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : redis_util.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-24 16:25
# @Copyright: 北京码同学
import javaobj
import redis


class RedisUtil:

    def __init__(self, host, pwd, port=6379, decode_responses=False, db=0):
        # 先创建一个连接池
        self.pool = redis.ConnectionPool(host=host, password=pwd, port=port, decode_responses=decode_responses, db=db)
        self.r = redis.Redis(connection_pool=self.pool)  # 从连接池里拿到一个连接对象
        # 通过连接对象，对redis进行操作

    def get(self, key):
        # 判断该key对应的数据类型是什么，然后决定要用哪个数据获取方法
        type = self.r.type(key).decode('utf-8')
        if type == 'string':
            return self.r.get(key)
        elif type == 'hash':
            return self.r.hgetall(key)
        elif type == 'list':
            return self.r.lrange(key, 0, -1)
        elif type == 'set':
            return self.r.smembers(key)
        elif type == 'zset':
            return self.r.zrange(key, 0, -1)
        else:
            raise Exception(f'{key}对应的数据类型不支持')


if __name__ == '__main__':
    redis_util = RedisUtil(host='121.42.15.146', pwd='testfan')
    # res = redis_util.get('{BUY_NOW_ORIGIN_DATA_PREFIX}_59') #59是用户id
    # # res得到的数据是商城项目向缓存中存储的一个java对象的序列化数据，我们无法直接从中得到想要的数据
    # # 所以我们需要先将该数据转换成python对象，然后再处理
    # print(res)
    # res_obejct = javaobj.loads(res)
    # print(res_obejct)
    # print(type(res_obejct))
    # print(res_obejct[0])
    # # 获取该对象下都有哪些属性信息,看到的业务属性需要和开发沟通是什么意思
    # print(dir(res_obejct[0]))
    # # 获取立即购买时存储到redis的num数量
    # print(res_obejct[0].__getattribute__('num'))
    # print(res_obejct[0].__getattribute__('skuId'))

    # 设置收货地址接口
    res = redis_util.get('{CHECKOUT_PARAM_ID_PREFIX}_59')  # 59是用户id
    # print(res)
    # res在redis里是个hash，对应的就是python里的字典，所以我们直接遍历他
    for key, value in res.items():
        # 将key转换
        key1 = javaobj.loads(key)
        # print(key1)
        # print(value)
        try:
            value1 = javaobj.loads(value)
            print(value1)
        except:
            pass
        if key1 == 'addressId':
            print(value1)
        elif key1 == 'paymentType':
            # 因为对应的value是个对象，
            print(dir(value1))
            print(value1.__getattribute__('constant'))
