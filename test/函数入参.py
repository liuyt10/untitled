a = 100


def a1():
    print(a)


def a2():
    global a
    a = 390
    print(a)

# *args 位置传参 是元组格式
# **kwargs 关键字传参  是字典格式
def userinfo1(name, age, gender, **kwargs):
    print(f'userinfo1:姓名:{name},年龄:{age},性别:{gender},其他信息:{kwargs}')


def userinfo2(name, age, gender, user='liu', **kwargs):
    print(f'userinfo2:姓名:{name},年龄:{age},性别:{gender},姓名:{user},其他信息:{kwargs}')


def userinfo3(name, age, gender, user, *args):
    print(f'userinfo3:姓名:{name},年龄:{age},性别:{gender},姓名:{user},其他信息:{args}')


def userinfo4(name, age, gender, *args, user='liu'):
    print(f'userinfo4:姓名:{name},年龄:{age},性别:{gender},姓名:{user},其他信息:{args}')


def userinfo44(name, age, gender, user='liu', *args):
    print(f'userinfo44:姓名:{name},年龄:{age},性别:{gender},姓名:{user},其他信息:{args}')


def userinfo5(*args, **kwargs):
    print(f'userinfo5:姓名:{args[0]},年龄:{args[1]},性别:{args[2]},姓名:{args[3]},其他信息:{kwargs}')


if __name__ == '__main__':
    # a1()
    # a2()
    userinfo1(name='shuju', age=17, gender='女', QQ='电脑散热', shuju='豪尔赫', xinxi='单人图')
    userinfo2(name='shuju', age=17, gender='女', gfsnj='电脑散热', shuju='豪尔赫', xinxi='单人图')
    userinfo3('shuju', 17, '女', '电脑散热', '豪尔赫', '单人图')
    userinfo4('shuju', 17, '女', '豪尔赫', '单人图')  # name, age, gender, *args, user='liu'
    userinfo44('shuju', 17, '女', '豪尔赫', '单人图')  # name, age, gender, user='liu', *args
    userinfo5('shuju', 17, '女', '豪尔赫', '最后一个', gfsnj='电脑散热', shuju='豪尔赫', xinxi='单人图')
