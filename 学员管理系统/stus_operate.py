from 学员管理系统.file_operate import FileOperate
from 学员管理系统.student import Student


class StuOperate:
    stu_dict = FileOperate.read()

    @classmethod
    def stu_add(cls, stu_obj):
        if stu_obj.id in cls.stu_dict:
            return '学员已存在，添加失败'
        else:
            cls.stu_dict[stu_obj.id] = stu_obj
            FileOperate.write(cls.stu_dict)
            return '添加成功'

    @classmethod
    def stu_del(cls, id):
        if id in cls.stu_dict:
            del cls.stu_dict[id]
            FileOperate.write(cls.stu_dict)
            return '删除成功'
        else:
            return '学生不存在，删除失败'

    @classmethod
    def stu_change(cls, id, **kwargs):
        if id in cls.stu_dict:
            if 'name' in kwargs:
                cls.stu_dict[id].name = kwargs['name']
            if 'phone' in kwargs:
                cls.stu_dict[id].phone = kwargs['phone']
            if 'score' in kwargs:
                cls.stu_dict[id].score = kwargs['score']
            if 'wx' in kwargs:
                cls.stu_dict[id].wx = kwargs['wx']
            if 'qq' in kwargs:
                cls.stu_dict[id].qq = kwargs['qq']
            FileOperate.write(cls.stu_dict)
            return '学生修改成功'

        else:
            return f'学生{id}不存在，修改失败'

    @classmethod
    def stu_find(cls, id):
        if id in cls.stu_dict:
            return str(cls.stu_dict[id])
        else:
            return f'学生{id}不存在'

    @classmethod
    def stu_average(cls):
        stu_sum = len(cls.stu_dict)
        total = 0
        for i in cls.stu_dict:
            stu_obj = cls.stu_dict[i]
            total += int(stu_obj.score)
        return total//stu_sum



