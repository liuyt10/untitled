# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : get_project_path.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 15:21
# @Copyright: 北京码同学


import os
# 得到该文件自身所处的目录其实就是项目路径
cur_path = os.path.abspath(__file__)
# print(cur_path)
project_path = os.path.dirname(cur_path)
# print(project_path)