# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : run.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 11:33
# @Copyright: 北京码同学

import os

import pytest

if __name__ == '__main__':
    # 会自动扫描当前目录下的pytest.ini
    # 根据配置文件中的配置来执行测试
    pytest.main()
    # 执行命令，生成测试报告
    os.system('allure generate ./report/data -o ./report/html --clean')
