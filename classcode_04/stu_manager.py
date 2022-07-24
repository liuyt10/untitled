# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : stu_manager.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 15:37
# @Copyright: 北京码同学

# 该文件是学员管理系统的入口文件
from lesson0703.student import Student
from lesson0703.stus_operate import StuOperate


def run():
    print('==============欢迎进入码同学学员管理系统==================')
    while True:
        op_type = int(input('请输入你的操作,1:新增 2:修改 3:删除 4:查询 5:退出 ：'))
        if op_type == 1:
            id = input('请输入学员id:')
            name = input('请输入学员姓名:')
            phone = input('请输入手机号:')
            stu = Student(id=id,name=name,phone=phone)
            print(StuOperate.add_stu(stu))
        elif op_type == 2:
            id = input('请输入学员id:')
            # {"wx":"wx2222","qq":"qq2222"} kwargs 需要输入成这种格式
            kwargs = input('请输入要修改的信息:')
            kwargs = eval(kwargs) #eval可以把字符串形式的字典转成字典类型
            print(StuOperate.change_stu(id, **kwargs))
        elif op_type == 3:
            id = input('请输入学员id:')
            print(StuOperate.delete_stu(id))
        elif op_type == 4:
            id = input('请输入学员id:')
            print(StuOperate.select_stu(id))
        elif op_type == 5:
            break
if __name__ == '__main__':
    run()