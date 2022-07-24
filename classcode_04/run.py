# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : run.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-03 16:48
# @Copyright: 北京码同学

import unittest

from lesson0703.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./','test_*.py')
    # 创建一个执行器,这种方式执行完之后很难分辨执行结果
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # 所以我们希望执行完成后能够得到一个测试报告
    with open(file='report.html',mode='wb') as f:
        HTMLTestRunner(f,title='学员管理系统测试报告',description='这只是个藐视').run(suite)