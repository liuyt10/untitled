# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : c02_class_attr_func_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 10:24
# @Copyright: 北京码同学

# 类属性和类方法
class Student:
    # 在类下面直接定义的变量叫做类属性
    # 当所有的对象都具备相同的属性值时，不会根据某个对象的属性变化而变化，要变大家统一都变
    # 相当于是一个全局性的变量
    school = '码同学'
    course = 'python自动化'
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
        Student.show_school() # 直接使用类名称调用类方法

    # 通过@classmethod标注的方法，表示的是类方法
    # cls表示的当前类
    # 注意：类方法中无法直接使用self去调用对象方法及对象属性
    @classmethod
    def show_school(cls):
        print(f'学校是{cls.school}')
if __name__ == '__main__':
    # 类属性的调用
    # 直接只用类名称即可调用类属性
    print(Student.school)
    # print(Student.name)
    stu1 = Student('张三',18,'3班')
    print(stu1.school) # 实例对象也可以调用类属性，但是通常不这么做
    stu1.school = 'testfan' # 使用对象去修改类属性,看起来像是在修改类属性，实际上是他动态的生成了一个对象属性，名字和类属性的名字一样
    print(stu1.school)
    stu2 = Student('李四',20,'4班')
    print(stu2.school)

    # 我使用类调用类属性直接修改
    Student.school = '码同学1'
    print(stu1.school)
    print(stu2.school)

    # 调用类方法，通过类名称去调用
    Student.show_school()
    stu1.show_school()
