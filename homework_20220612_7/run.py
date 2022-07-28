# encoding: utf-8 -*-


# 登录用户、查询订单、生成订单、确认订单、发货、待收货、确认收货、待付款、已付款、完成
import sys

from homework_20220612_7.buyer_operate import buyer_Operate
from homework_20220612_7.seller_operate import seller_Operate


menu = '''
    1.买家系统     
    2.卖家系统
    '''
while True:
    print(menu)
    user_info = input('请输入你需要进入的系统，输入q退出>>:')
    if user_info == '1':
        buyer_Operate()
    elif user_info == '2':
        seller_Operate()
    elif user_info.lower() == 'q':
        print('感谢使用，欢迎您的下次光临')
        sys.exit()
    else:
        print('你的输入不正确，请重新输入')
