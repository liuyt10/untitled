# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : test_ddt.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 16:33
# @Copyright: 北京码同学
import unittest

import ddt

from lesson0703.stus_operate import StuOperate

@ddt.ddt # 当采用了ddt时，则不能使用鼠标右键在当前类上执行，必须使用unittest.main()去执行
class TestChangeStu(unittest.TestCase):

    # def test_change_name(self):
    #     msg = StuOperate.change_stu('7',name='shamo')
    #     assert msg == '修改成功'
    # def test_change_phone(self):
    #     msg = StuOperate.change_stu('7',phone='1872727')
    #     assert msg == '修改成功'
    # def test_change_id_not(self):
    #     msg = StuOperate.change_stu('13',phone='1872727')
    #     assert msg == '13不存在'
    # def test_change_not_attr(self):
    #     msg = StuOperate.change_stu('7')
    #     assert msg == '修改成功'

    test_data = [
        ['7', {'name': '张三'}, '修改成功'],
        ['7', {'phone': '1872456'}, '修改成功'],
        ['7', {'wx': 'wx002'}, '修改成功'],
        ['7', {'qq': 'qq002'}, '修改成功'],
        ['7', {'score': '90'}, '修改成功'],
        ['13', {'wx': 'wx002'}, '13不存在1']
    ]
    # ddt数据参数的第三方库，先安装ddt
    # windows： pip  install  ddt
    # mac: python3 -m pip install ddt
    @ddt.data(*test_data)
    def test_change_stu(self,data): # 这个data就表示了test_data中的每一组数据
        id = data[0]
        kwargs = data[1]
        expect_msg = data[2]
        msg = StuOperate.change_stu(id,**kwargs)
        assert msg == expect_msg
if __name__ == '__main__':
    unittest.main()

