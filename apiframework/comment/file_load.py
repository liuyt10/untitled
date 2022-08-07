# -*- coding:utf-8 -*-
import pandas
import yaml

from get_project_path import project_path


def read_excel(filepath, sheet_name):
    # keep_default_na该参数默认是True，意思是读取空单元格结果是na,但是我们不希望空单元格读取出来是na，所以我们设置成False
    # 那么空单元格读取后就是空字符串
    # engine是执行引擎，openpyxl是第三方库
    res = pandas.read_excel(f'{project_path}{filepath}', sheet_name=sheet_name, keep_default_na=False,
                            engine='openpyxl')
    # print(res.shape)
    lines_count = res.shape[0]  # 结果总行数
    cols_count = res.shape[1]  # 结果总列数
    # data是用来存储我们转换之后的结果数据
    data = []
    for l in range(lines_count):
        line = []
        for i in range(cols_count):
            cell_data = res.iloc[l, i]
            line.append(cell_data)
        data.append(line)
    return data


def load_yaml_file(filepath):
    with open(file=f'{project_path}{filepath}', mode='r', encoding='utf-8') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)  # Loader表示加载方式，选择全部加载
        return yaml_content


if __name__ == '__main__':
    # print(read_excel(r'E:\project\untitled\apiframework\data\mtxshop_testdata.xlsx', '立即购买数据'))
    print(load_yaml_file('/data/mtshop_testdata.yml')['创建交易']['client'])
    print(load_yaml_file('/data/mtshop_testdata.yml')['立即购买'])
