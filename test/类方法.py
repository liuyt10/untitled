# encoding: utf-8 -*-

# map 高阶函数
from functools import reduce

from lesson.core.Manager import Manager

list1 = [10, 20, 30, 10, -70]


# list2 = []
# for i in list1:
#     list2.append(i*2)
# print(list2)

# list2 = map(lambda n: n ** 2, list1)
# print(set(list2))
# list3 = filter(lambda n: n % 3 == 0, list1)
# print(list(list3))
# result = reduce(lambda x, y: x - y, list1)  # 计算上述列表中所有项乘起来的结果
# print(result)
# stus = [{'name': '王五', 'score': 60}, {'name': '李四', 'score': 85}, {'name': '张三', 'score': 90}]
# result = sorted(stus, key=lambda stu: stu['score'])
# print(result)
# stus = 'gsngnh'
# result = sorted(stus, key=lambda stu: stu)
# print(result)
# stus = ['909', '56', 'rt', '1', 'a', "A"]
# result = sorted(stus, key=lambda stu:stu)
# print(result)


# with open(file='test.txt', mode='a', encoding='utf-8') as f:
#     list1 = ['\nbskjhvf','\naaaaaa']
#     # f.write(list1)  #只能写入一组
#     f.writelines(list1)  #写入多组

# with open(file='test.txt', mode='r', encoding='utf-8') as f:
#     print(f.read())  #读取全部内容,以字符串格式存放
# print(f.readlines())  # 读取全部内容,存放至列表中
# print(f.readline().strip())  # 每次读取一行
# print(f.readline().strip())  # 每次读取一行
# print(f.readline().strip())  # 每次读取一行


# 异常：通过希望代码碰到异常也能继续处理，不影响整个流程的执行

# try:
#     l = [1, 2]
#     print(l[2])
# except BaseException as e:
#     print(f'索引异常{e}')
# finally:
#     print('执行完毕')


# try:
#     print('执行时try里面的代码没有报错就会执行后面的else')
#
# except:
#     print('try里面报错了就执行except')
#
# else:
#     print('try里面没有报错就执行else')


# def add(a,d):
#     if type(a)  == type(d):
#         return a+d
#     else:
#         raise TypeError(f'{a}和{d}类型不一致')
#         # raise BaseException(f'{a}和{d}类型不一致')
#
# # add(1,'sd')
#
# try:
#     add(1,'sd')
# # except BaseException as e:
# except BaseException as e:
#     print(f'类型不行，换一组数据:{e}')
# print('计算完成')


class Plane:
    school = 'family'
    teacher = 'shujuxinxi '

    def __init__(self, num, height):
        self.num = num
        self.height = height
        self.lenth = 100
        self.weith = 50

    def fly(self, h):
        print(f'{self.num}起飞了,起飞高度是{h}')

    def __str__(self):  # 针对对象做str类型转换时，也会自动调用该方法
        # return {self.num},{self.height}
        return f'{self.num},{self.height}'
    @classmethod
    def show_school(cls):
        print(f'学校是{cls.school}')


if __name__ == '__main__':
    plane1 = Plane('23y4', '111')
    plane2 = Plane('2222', '222')
    plane2.show_school()
    plane3 = Manager('sgh')
    plane3.creatTeacher()
    # print(plane1)
    # # s = str(plane1)
    # # print(s)
    # plane.fly(200)
    # print(Plane.school)
    # print(plane1.school)
    # plane1.school = 'gerg'
    # print(plane1.school)
    # Plane.school = '1112'
    # print(plane1.school)
    # print(plane2.school)
