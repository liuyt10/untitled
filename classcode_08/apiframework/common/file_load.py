# !/usr/bin python3                                 
# encoding: utf-8 -*-   
# @file     : file_load.py                       
# @author   : 沙陌 Matongxue_2
# @Time     : 2022-07-31 14:45
# @Copyright: 北京码同学
import pandas
import yaml

from get_project_path import project_path


def read_excel(filepath,sheet_name):
    # keep_default_na该参数默认是True，意思是读取空单元格结果是na，我们不希望是na，所以设置成False
    # 那么空单元格读取后就是空字符串
    res = pandas.read_excel(f'{project_path}{filepath}',sheet_name=sheet_name,keep_default_na=False,engine='openpyxl')
    # print(res)
    # 从这里开始，下面的代码都是为了将读到的结果转换成pytest能够识别的数据结构
    lines_count = res.shape[0] # 结果总行数
    cols_count = res.shape[1] # 结果总列数
    # data就是用来存储我们转换之后的结果的数据
    data = []
    for l in range(lines_count):
        line = []
        for c in range(cols_count):
            # 获取单元格数据
            cell_data = res.iloc[l,c] # 根据行和列得到某个单元格数据
            line.append(cell_data)
        data.append(line)
    return data

def load_yaml_file(filepath):
    with open(file=f'{project_path}{filepath}',mode='r',encoding='UTF-8') as f:
        yaml_content = yaml.load(f,Loader=yaml.FullLoader)
        return yaml_content
if __name__ == '__main__':
    # print(read_excel('/data/mtxshop_testdata.xlsx', '立即购买数据'))
    print(load_yaml_file('/data/mtxshop_testdata.yml')['创建交易']['client'])
    print(load_yaml_file('/data/mtxshop_testdata.yml')['立即购买'])