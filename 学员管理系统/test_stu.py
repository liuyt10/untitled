# -*- coding:utf-8 -*-
import unittest

# 如果想要用unittest进行测试，需要继承unittest.TestCase
from 学员管理系统.student import Student
from 学员管理系统.stus_operate import StuOperate


class TestAddStu(unittest.TestCase):
    #前置处理，每条测试用例执行前都会执行
    def setUp(self) -> None:
        print('每条用例执行前都会执行')
        StuOperate.stu_del(35)
        stu = Student(1, '苏某某', '1778950')

    #后置处理，每条测试用例执行后都会去执行
    def tearDown(self) -> None:
        print('每条用例执行后都会执行')


    #前置处理，当前类执行用例前只执行一次
    @classmethod
    def setUpClass(cls) -> None:
        print('当前类执行前只执行一次')

    #后置处理，当前类执行后只执行一次
    @classmethod
    def tearDownClass(cls) -> None:
        print('当前类执行后只执行一次')
    # 测试类下可以多个测试函数，一个测试函数就是一个用例
    def test_add1(self):
        # 所谓的测试其实就是调用目标方法，传递测试数据，判断方法返回的结果是否符合预期
        stu = Student(35, '李某某', '1778950')
        msg = StuOperate.stu_add(stu)
        # msg是否是  添加成功，判断结果是否正确的过程叫做断言
        assert msg == '添加成功'
    #测试学员添加失败
    def test_add2(self):
        stu = Student(1, '苏某某', '1778950')
        msg = StuOperate.stu_add(stu)
        # msg是否是  添加成功，判断结果是否正确的过程叫做断言
        assert msg == '学员已存在，添加失败'


