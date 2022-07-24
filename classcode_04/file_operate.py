# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : file_operate.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 13:49
# @Copyright: 北京码同学

# 在这里专门来封装txt文件的读取和写入
from lesson0703.student import Student


class FileOperate:

    def __init__(self):
        self.file_path = r'D:\pycharmprojects\python0612\pythonbasic\lesson0703\students.txt'


    def read(self):
        # 读取文件
        # 读到的内容需要以什么样的数据结构进行存储，才方便后续处理
        # {id1:stu1,id2:stu2,id3:stu3}
        # 以字典作为读取到的数据存储形式，字典的key表示每个学员的id，字典的value表示每个学员对象
        stus_dict = {}
        with open(file=self.file_path,mode='r',encoding='UTF-8') as f:
            all_lines = f.readlines() #读取所有行
            print(all_lines)
            for line in all_lines:
                # line = '1,张三,1872663,wx0001,xxxxx\n'
                line_split = line.split(',')
                id = line_split[0]
                name = line_split[1]
                phone = line_split[2]
                wx = line_split[3]
                qq = line_split[4].strip()
                # 根据解析出的学员信息，创建学员对象
                stu = Student(id,name,phone,wx,qq)
                stus_dict[id] = stu
        return stus_dict
    # {id1:stu1,id2:stu2,id3:stu3}
    def write(self,stus_dict:dict):
        # 不管修改哪个，我都全部重新写入
        with open(file=self.file_path,mode='w',encoding='UTF-8') as f:
            for stu in stus_dict.values():
                # stu在这里代表的学员对象，写入时我们希望写入的学员信息是
                # 1,张三,1872663,wx0001,xxxxx 形式
                f.write(str(stu))
                f.write('\n')

if __name__ == '__main__':
    # a1 = FileOperate()
    # a1.read()
    # a2 = FileOperate()
    stus_dict = FileOperate().read()
    # FileOperate().write(stus_dict)
    a = FileOperate()
    a.file_path = r'D:\pycharmprojects\python0612\pythonbasic\lesson0703\students1.txt'
    a.write(stus_dict)
