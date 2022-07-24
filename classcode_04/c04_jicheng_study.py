# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : c04_jicheng_study.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 11:18
# @Copyright: 北京码同学

# 继承可以帮我们减少代码重复，提升代码复用效率

class Animal:
    s = 'aaaa'
    def __init__(self,name):
        self.name = name

    def eat(self,s):
        print(f'吃{s}')

class Dog(Animal): # 类名称后面小括号里写了其他类名称，表示当前类继承了小括号里的类

    # 父类中虽然定义了初始化的属性只有name
    # 但是我自己要在这个属性的基础上进行扩展
    def __init__(self,name,color):
        # 要先调用父类的初始化方法，便于集成父类的东西
        super().__init__(name)
        # self.name = name
        self.color = color
    # pass
    # def __init__(self,name):
    #     self.name = name
    #
    # def eat(self,s):
    #     print(f'吃{s}')
    # 当子类方法名称和父类的方法名称相同时，这种现象是多态的一种表现
    def eat(self,s,n):
        print(f'吃了{n}斤{s}')
    def sleep(self):
        print(f'{self.name} 正在睡觉')


class Cat(Animal):
    pass
    # def __init__(self,color):
    #     self.color = color
    # def eat(self,s):
    #     print(f'吃{s}')
if __name__ == '__main__':
    dog = Dog('癞皮狗','灰色')
    dog.eat('骨头',1)
    print(Dog.s)
    Dog.s = 'BBBBB'
    cat = Cat('咖啡猫')
    print(cat.name)
    cat.eat('鱼')
    print(Cat.s)