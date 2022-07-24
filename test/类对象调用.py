# a = 10 / 2
# b = 10 * 3
# c = 10 % 6  # 取余
# d = 27 // 7  # 取整
# print(f'{a},{b},{c},{d}')
# print(a)

# x = int(input('请输入一个数字：'))
# # if x % 2 == 0:
# # #     print(f'{x}是偶数')
# # # else:
# # #     print(f'{x}是奇数')
# if x>90:
#     print('优秀')
# elif x>80:
#     print('良好')
# elif x>70:
#     print('一般')
# elif x > 60:
#     print('及格')
# else:
#     print('不及格')
# # #
# # # season = input('请输入现在的季节：')
# # # if season == '春天':
# # #     print('春雨惊春清谷天')
# # # elif season == '夏天':
# # #     print('夏满芒夏暑相连')
# # # elif season == '秋天':
# # #     print('秋处露秋寒霜降')
# # # elif season == '冬天':
# # #     print('冬雪雪冬小大寒')
# # # else:
# # #     print('你的输入不正确，请重新输入')
# #
# # i = 1
# # sum = 0
# # while i<=100:
# #     # while i == 67:
# #     #     i += 1
# #     #     continue
# #     sum += i
# #     i += 1
# # print(sum)
#
# L = ['alex','shuxue','xinxi','keji']

# def func(item):
# #     return item + '_sb'
# # ret = map(func,L)
# # for i in ret:
# #     print(i)
# # print(i)
# # print(i)
#
# import sys
# sys.setrecursionlimit(1000000)
#
# n = 0
#
# def story():
#     global n
#     n += 1
#     print(n)
#     story()
# story()
#
#
#
# def is_add(x):
#     return x%2==1
# print(list(filter(is_add,[1,2,3,4,5,6])))
# import re
# ret = re.search('\d(\w)+','dshuiw34556vbewjvbk')
# print(ret.group(1))
# import queue
#
# q = queue.Queue()
# q.put(10)
# q.put(5)
# q.put(2)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# import random
# def v_code():
#     code = ''
#     for i in range(5):
#         num = random.randint(0,9)
#         alf = random.randint(65,90)
#         add = random.choice([num,alf])
#         code = ''.join([code,str(add)])
#
#     return code
# print(v_code())

# import sys
# print(sys.platform)
# print(sys.version)

# a = {'suizhan':'shuju'}
# print([a],type([a]))
# class Foo:
#     count = 1
#     def __init__(self):
#         pass
#
# f1 = Foo()
# f2 = Foo()
# print(f1.count)
#
# class Goods:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price*0.5
#     def func(self):
#         return(self.age)
#
#
# good = Goods('苹果',5)
# print(good.price)
# good.age = 18
# print(good.func())
#
# isinstance(good,Goods)
# print(good)

# print('%(key)s'%{'key':'valueugkj'})
# print('%s  %s'%('key','value'))
#
# s ="hgaoegnjcjksznlknciuehvnaskd"
# l = [i for i in s]
# print(l)
set_week = {'周一': 'v1', '周二': [1, 2, 3], ('周三', '周日'): '{v2}'}
for i in set_week:
    if type(set_week[i]) is list:
        print(i)
for i in set_week:
    if type(i) == tuple:
        print(set_week[i])

