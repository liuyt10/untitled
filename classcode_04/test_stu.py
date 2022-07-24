# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_stu.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 16:14
# @Copyright: 北京码同学
import unittest

from lesson0703.student import Student
from lesson0703.stus_operate import StuOperate


class TestAddStu(unittest.TestCase):
    # 针对测试用例来说，可能需要在测试前去准备测试数据，或者测试后去清除测试数据
    # 前置处理
    def setUp(self) -> None:
        print('每条测试用例执行前都会被执行')
        StuOperate.delete_stu('4')
        stu = Student('1','李四','19892882')
        msg = StuOperate.add_stu(stu)
    # 后置处理
    def tearDown(self) -> None:
        print('每条用例执行后都会去执行')

    @classmethod
    def setUpClass(cls) -> None:
        print('当前类执行前只执行一次')
    @classmethod
    def tearDownClass(cls) -> None:
        print('当前类所有用例执行完后，只执行一次')

    # 测试  新增学员成功
    def test_add1(self):
        # 所谓的测试其实就是调用目标方法，传递测试数据，判断方法返回结果是否符合预期
        stu = Student('4','李四','19892882')
        msg = StuOperate.add_stu(stu)
        # msg是否是 添加成功，判断结果是否正确的这个过程我们叫做断言
        assert msg == '添加成功'
    # 测试学员添加失败
    def test_add2(self):
        stu = Student('1','李四','19892882')
        msg = StuOperate.add_stu(stu)
        # msg是否是 添加成功，判断结果是否正确的这个过程我们叫做断言
        assert msg == '学员添加失败'
