# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : c03_static_method_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 11:05
# @Copyright: 北京码同学

class Student:

    def __init__(self,name,age,banji,score=0):
        self.name = name
        self.age = age
        self.banji = banji
        self.score = score
    # 默认情况下，打印对象时，会打印对象对应的内存地址
    # 但是我想让学员对象打印时直接打印出他的基本信息:张三,18,3班,85
    # 该方法在print(对象)时，会被默认自动调用
    # 当针对对象做str类型转换时，也会自动调用该方法
    def __str__(self):
        return f'{self.name},{self.age},{self.banji},{self.score}'
        # return self.name,self.age

    def show_name(self):
        print(f'我的名字是:{self.name}')
    def show_age(self):
        print(f'我的年龄是:{self.age}')
    def set_name(self,name):
        self.name = name
    def show_banji(self):
        print(f'我的班级是:{self.banji}')

    # 使用@staticmethod标注的方法，叫做静态方法
    # 那么静态方法的参数里没有cls，也没有self，他其实和普通函数没有什么区别
    # 仅仅只是为了按照一定分类规则，把这个函数放在了类下面进行管理
    @staticmethod
    def avg_score(stu_list:list):
        sum = 0
        count = len(stu_list)
        for stu in stu_list:
            sum += stu.score
        return sum/count
# def avg_score(stu_list:list):
#     sum = 0
#     count = len(stu_list)
#     for stu in stu_list:
#         sum += stu.score
#     return sum/count
if __name__ == '__main__':
    # 静态方法调用也是使用类名称加上静态方法名称
    # 创建三个学员对象
    stu1 = Student('张三',18,'3班',score=90)
    stu2 = Student('李四', 18, '3班', score=80)
    stu3 = Student('王五', 18, '3班', score=85)
    stu_list = [stu1,stu2,stu3]
    print(Student.avg_score(stu_list))
    print(stu1.avg_score(stu_list))
    # print(avg_score(stu_list))
