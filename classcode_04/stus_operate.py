# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : stus_operate.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 14:47
# @Copyright: 北京码同学
from lesson0703.file_operate import FileOperate
from lesson0703.student import Student


class StuOperate:

    # 所有学员的信息实际上我们是存在文件中，但是文件不好直接操作
    # 所以我们从文件中读取所有数据存入到一个字典中，操作字典是比较方便的，操作完成后写入文件
    stus_dict = FileOperate().read() # {id1:stu1,id2:stu2,id3:stu3}

    # 新增
    @classmethod
    def add_stu(cls,stu:Student):
        # 判断新增的学员id是否已经存在，如果不存在则添加，存在则添加失败
        if stu.id in cls.stus_dict:
            return f'学员添加失败'
        else:
            cls.stus_dict[stu.id] = stu
            FileOperate().write(stus_dict=cls.stus_dict)
            return '添加成功'

    # 删除
    # 根据学员id进行删除，所以id是动态数据，做为参数传递
    @classmethod
    def delete_stu(cls,id):
        if id in cls.stus_dict:
            del cls.stus_dict[id]
            FileOperate().write(cls.stus_dict)
            return '删除成功'
        else:
            return f'{id}不存在'

    # 查询学员
    # 通过id查询学员，所以id可以作为入参
    @classmethod
    def select_stu(cls,id):
        if id in cls.stus_dict:
            return str(cls.stus_dict[id])
        else:
            return f'{id}不存在'

    # 修改学员
    # 通过id可以确定我要修改的学员是谁，所以第一个参数是id
    # 你还得告诉我要修改学员的什么信息，修改成什么值
    # name/phone/wx/qq并不确定本次要修改哪几个属性
    @classmethod
    def change_stu(cls,id,**kwargs):
        """

        :param id:
        :param kwargs:
        :return:
        """
        if id in cls.stus_dict:
            stu = cls.stus_dict[id] # 得到我要修改的学员对象
            # 不定长关键字传进来后的类型是字典
            # 解析kwargs这个字典，来判断他到底要修改什么东东
            if 'name' in kwargs:
                attr_value = kwargs['name'] # 获取你传进来的name对应的值
                # 修改目标学员对象的name属性
                stu.set_name(attr_value)
            if 'phone' in kwargs:
                attr_value = kwargs['phone'] # 获取你传进来的phone对应的值
                # 修改目标学员对象的phone属性
                stu.set_phone(attr_value)
            if 'wx' in kwargs:
                attr_value = kwargs['wx'] # 获取你传进来的wx对应的值
                # 修改目标学员对象的wx属性
                stu.set_wx(attr_value)
            if 'qq' in kwargs:
                attr_value = kwargs['qq'] # 获取你传进来的qq对应的值
                # 修改目标学员对象的name属性
                stu.set_qq(attr_value)
            # 重新写入数据文件
            FileOperate().write(cls.stus_dict)
            return '修改成功'
        else:
            return f'{id}不存在'
if __name__ == '__main__':
    # stu1 = Student('6','张三','7177633')
    # print(StuOperate.add_stu(stu1))
    StuOperate.delete_add('6')
    print(StuOperate.select_stu('5'))
    # StuOperate.change_stu('3',name='沙陌',phone='1890001',wx='wx1111',qq='qq1111')
    info = {'wx':'wx2222','qq':'qq2222'}
    StuOperate.change_stu('3',**info)