# encoding: utf-8 -*-

# 学生管理系统的入口
from 学员管理系统.file_operate import FileOperate
from 学员管理系统.student import Student
from 学员管理系统.stus_operate import StuOperate


def run():
    print('=================欢迎进入学生管理系统===================')
    stu_dict = FileOperate.read()
    while True:
        operate_info = int(input('请输入您要进行的操作：1.增加学员 2.删除学员 3.修改学员 4.查询学员 5:查看全班平均分 6:退出:'))
        if operate_info == 1:  # 增加学员
            id = int(input('请输入需要增加的学生的id:'))
            name = input('请输入需要增加的学生的姓名:')
            phone = input('请输入需要增加的学生的手机号:')
            score = input('请输入需要增加的学生的成绩:')
            wx = input('请输入需要增加的学生的微信:')
            qq = input('请输入需要增加的学生的QQ号:')
            studen = Student(id, name, phone, score, wx, qq)
            print(StuOperate.stu_add(studen))

        elif operate_info == 2:  # 删除学员
            stu_id = int(input('请输入你需要删除的学员id:'))
            print(StuOperate.stu_del(stu_id))

        elif operate_info == 3:  # 修改学员
            stu_id = int(input('请输入需要修改的学生id:'))
            kwargs = input('请输入需要修改的信息:')
            kwargs = eval(kwargs)
            print(StuOperate.stu_change(stu_id, **kwargs))
        elif operate_info == 4:  # 查询学员
            stu_id = int(input('请输入需要查询的学生id:'))
            print(StuOperate.stu_find(stu_id))
        elif operate_info == 5:  # 查询全班平均分
            print(StuOperate.stu_average())
        elif operate_info == 6:  # 退出
            print('您已退出学生管理系统')
            break
        else:
            print('您的输入有误，请重新输入')


if __name__ == '__main__':
    run()
