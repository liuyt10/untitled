# _*_ coding: utf-8 _*_

def func(x):
    if x == 1 or x ==2:
        return 1
    elif x>2:
        return func(x-1)+func(x-2)

def shizi(x):
    if x==1:
        return 1
    elif x>1 :
        ret1 = func(x)/func(x+1)
        return ret1+shizi(x-1)
    else:
        return ('序列项数不能为负数')

try:
    ret = int(input("请输入你要相加的序列项数："))
    print(shizi(ret))
except:
    print("输入错误，请输入正整数")