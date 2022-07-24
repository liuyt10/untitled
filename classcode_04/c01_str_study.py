# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : c01_str_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 10:11
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
if __name__ == '__main__':
    stu1 = Student(name='张三',age=20,banji='3班',score=85)
    # print(stu1)
    s = str(stu1)
    print(s)
    # stu1.show_name() # 张三
    # stu1.set_name('张三三')
    # stu1.show_name() # 张三三
    stu2 = Student('李四',18,'4班')
    stu2.score = 88
    print(stu2)