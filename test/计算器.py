import re

ss = '9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14'
a = '1 - 2 * ( ( 6 0 -3 0  +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
new_a = a.replace(' ', '')

# 去掉所有的空格
# 加减乘除  括号
# 先算括号里的乘除，再算括号里的加减
# 从括号里取值 == 正则表达式
def dealwith(exp):
    exp = exp.replace('+-','-')
    exp = exp.replace('--','+')
    return exp

def cal_exp_son(exp_son):
    # 只用来计算原子型的表达式，两个数之间的乘除法
    if '/' in exp_son:
        a, b = exp_son.split('/')
        return str(float(a)/float(b))
    elif '*' in exp_son:
        a, b = exp_son.split('*')
        return str(float(a)*float(b))


def cal_express_no_bracket(exp):
    # 计算没有括号的表达式
    # exp是没有经过
    exp = exp.strip('()')
    # 先乘除后加减
    while True:
        ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', exp)  #匹配第一个乘除
        if ret:
            exp_son = ret.group()  # 子表达式，最简单的乘除法
            print(exp_son)
            ret = cal_exp_son(exp_son)  #计算子表达式的乘除后，得出结果
            exp = exp.replace(exp_son,ret) #将子表达式中计算的结果，替换进表达式中
            exp = dealwith(exp)
            print(exp)
        else:
            ret = re.findall('-?\d+\.?\d*',exp)
            print('*****',ret)
            sum = 0
            for i in ret:
                sum += float(i)
            return str(sum)

while True:
    ret = re.search('\([^()]+\)', new_a)
    if ret:
        a_no_bracker = ret.group()  # 表达式，没括号
        print('内部不在有括号的值：',a_no_bracker)
        ret = cal_express_no_bracket(a_no_bracker)
        new_a = new_a.replace(a_no_bracker,ret)
        new_a = dealwith(new_a)
        print(new_a)
    else:
        print('表达式中已经没有括号了',new_a)
        ret = cal_express_no_bracket(new_a)
        print(ret)
        break
