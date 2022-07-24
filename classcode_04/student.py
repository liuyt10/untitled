# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : student.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 13:42
# @Copyright: 北京码同学


class Student:


    def __init__(self,id,name,phone,wx='',qq=''):
        self.id = id
        self.name = name
        self.phone = phone
        self.wx = wx
        self.qq = qq
    def __str__(self):
        return f'{self.id},{self.name},{self.phone},{self.wx},{self.qq}'
    # 修改及获取各个属性
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_phone(self):
        return self.phone
    def set_phone(self,phone):
        self.phone = phone
    def get_wx(self):
        return self.wx
    def set_wx(self,wx):
        self.wx = wx
    def get_qq(self):
        return self.qq
    def set_qq(self,qq):
        self.qq = qq



if __name__ == '__main__':
    stu1 = Student('1','张三','7177633')
    # print(StuOperate.add_stu(stu1))