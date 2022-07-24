# -*- coding:utf-8 -*-
import unittest

import ddt as ddt

from 学员管理系统.stus_operate import StuOperate


@ddt.ddt  # 当采用了ddt时，则不能使用鼠标右键在当前类上执行，必须使用unittest。main（）去执行
class TestChangeStu(unittest.TestCase):
    # def test_change_name(self):
    #     msg = StuOperate.stu_change(17, name='大约在冬季')
    #     assert msg == '学生修改成功'
    #
    # def test_change_phone(self):
    #     msg = StuOperate.stu_change(226, phone='9999999')
    #     assert msg == '学生修改成功'
    #
    # def test_change_id_not(self):
    #     msg = StuOperate.stu_change(1010, phone=12121121)
    #     assert msg == '学生不存在，修改失败'
    #
    # def tets_change_not_attr(self):
    #     msg = StuOperate.stu_change(17)
    #     assert msg == '修改成功'

    test_data = [[1, {'name': '李某某'}, '学生修改成功'],
                 [2, {'name': '王五'}, '学生修改成功'],
                 [3, {'name': '张三'}, '学生修改成功'],
                 [4, {'name': 'hgeruhg'}, '学生修改成功'],
                 [17, {'name': '丽丽'}, '学生修改成功'],
                 [220, {'name': '丽萨'}, '学生220不存在'],
                 [12, {'name': '钟离'}, '学生修改成功'],
                 [226, {'name': '香菱'}, '学生修改成功'],
                 [245, {'name': '皇女'}, '学生修改成功'],
                 [256, {'name': '班尼特'}, '学生修改成功'],
                 [23, {'name': '阿贝多'}, '学生修改成功']]

    @ddt.data(*test_data)  # test_datab表示需要传入的数据，单独的*表示拆列表，将列表拆成一个一个的列表数据
    def test_change_stu(self, data):  # data表示了test_data中的每一组数据
        id = data[0]
        kwarg = data[1]
        expect_msg = data[2]
        msg = StuOperate.stu_change(id, **kwarg)  # **表示拆字典，将字典拆成一个个的键值对
        assert msg == expect_msg


if __name__ == '__main__':
    unittest.main()
