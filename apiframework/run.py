# -*- coding:utf-8 -*-
import os

import pytest

if __name__ == '__main__':
    # 会自动扫描当前目录下的pytest.ini
    # 根据配置文件中的配置来执行测试
    pytest.main()
    # 执行命令，生成测试报告
    os.system('allure generate ./report/data -o ./report/html --clean')