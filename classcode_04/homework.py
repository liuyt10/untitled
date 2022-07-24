# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : homework.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 9:32
# @Copyright: 北京码同学


def days(year,month,day):
    sum_days = 0  # 初始化总天数变量
    # 统计month之前的所有月份的总天数
    for i in range(1, month):  # i是循环变量，在这里就代表你要循环叠加的月份
        print(i)
        # 判断当前月份的天数，然后给sum_days加上当前月的天数
        # 学了列表之后可以修改
        # if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
        if i in [1, 3, 5, 7, 8, 10, 12]:
            sum_days = sum_days + 31
        elif i in (4, 6, 9, 11):
            # elif i==4 or i==6 or i==9 or i==11:
            sum_days = sum_days + 30
        elif i == 2:
            # 2月份的时候要判断闰年
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                sum_days = sum_days + 29
            else:
                sum_days += 28
        else:
            print('月份不对')
    sum_days = sum_days + day
    print(f'{year}年{month}月{day}日是{year}年的第{sum_days}天')
def get_count_name(stus_list):
    # stus_list = [{'name': '张三', 'score': 45}, {'name': '李四', 'score': 57}, {'name': '王五', 'score': 80}]
    # 遍历列表，挨个判断学员分数是否小于60，如果小于60计数器加1，并打印他的姓名
    count = 0  # 计数器
    for stu in stus_list:
        # stu 是个字典，代表的是 {'name':'张三','score':45}
        score = stu['score']  # 得到当前学员成绩
        if score < 60:
            count += 1
            print(stu['name'])
    print(f'不及格的学员数量是:{count}')

def convert_list_lower(l):
    # l = ['Hello', 'World', 18, 'Apple', None]
    l_new = []
    for data in l:
        if type(data) == str:
            data = data.lower()
        #     l_new.append(data)
        #     # print(data)
        # else:
        #     l_new.append(data)
        l_new.append(data)
    print(l_new)
    return l_new

class Student:

    def __init__(self,name,age,banji,score=0):
        self.name = name
        self.age = age
        self.banji = banji
        self.score = score

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
    stu1.show_name() # 张三
    stu1.set_name('张三三')
    stu1.show_name() # 张三三
    stu2 = Student('李四',18,'4班')
    stu2.score = 88

    # 给学员增加成绩属性，
