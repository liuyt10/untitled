# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : c05_module_and_package_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 11:39
# @Copyright: 北京码同学

# 一个python文件就是一个python模块
# 一个package就是一个包，包主要是用来按照一定的规则将我们的模块代码进行分类管理，方便我们快速的查阅
# 要注意普通目录和包的区别，包里会有一个默认的__init__.py文件，该文件是这个包初始化时做的事情，通常不用管但是得有，否则导包就会出现问题


# 导包，当你用到的函数或者类或者变量，不在当前文件中时，就需要导入
from c04_jicheng_study import Dog #从c04这个模块中导入Dog类
from lesson0626.c01_func_study import find_last_only_one

dog = Dog('癞皮狗','白色')

# 如果你记得要导入的类、函数、变量等等的名称，可以写出来，然后使用alt+enter的快捷方式自动提示导包
find_last_only_one('shjhsdhdhd')

from c02_class_attr_func_study import Student as Student02
from c03_static_method_study import Student as Student03

stu02 = Student02('张三',18,'3班')
stu03 = Student03('张三',18,'3班')

# 1a = 'ss'
# class = 'hdhdh'
# A = 'aa'
# a = 'shhs'
# class StudentMaTongXue:
#     def nameAndAge(self):
#         pass
#     def name_and_age(self):
#         pass