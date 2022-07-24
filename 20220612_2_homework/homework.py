# _*_ coding: utf-8 _*_
# endstr = ''
# str1 = input("请输入你要查询的字符串：")
# for i in list(str1):
#     if str1.count(i) == 1:
#         endstr = i
# print(f"数列中只出现过一次且是最后的一个数字的字符是{endstr}，下标是{str1.index(endstr)}")
# s = '1080*1920'
# print(s[:-4:-1])
# print(s[::-1])
# s.replace('1','')
# len(s)
# s = ['张三','王五',12,34]
# s.reverse()
# s = [1,4,6]
# s1 = [9,2,5,0,100]
# s3 = s + s1
# s3.sort(reverse=True)
# print(s3)
# print(''.join(s))
# count = 0
# student =['三一_张三', '三一_张思', '三一_王五', '三一_张权', '三一_张一一']
# for i in student:
#     slt = i.split("_")
#     if slt[1].startswith('张'):
#         count += 1
#
# print(count)
# s = '  *shuju*信息  '
# print(s.split('*'))
#
#
# students =[ ['三一_张三', '三一_张思', '三一_王五', '三一_张权', '三一_张一一'],['三二_张三', '三二_张思', '三二_王五', '三二_张权', '三二_张一一'],['三三_张三', '三三_张思', '三三_王五', '三三_张权', '三三_张一一']]
#
# for i in range(len(students)):
#     for j in range(len(students[i])):
#         students[i][j] = f'清华附中_{students[i][j]}'
# print(students)

#
# tuple1 = (1,2,3,5,[5,7,3],'shuuju')
# tuple1[4][1] = 100
# print(tuple1)
#
# tuple2 = ('ss')
# print(type(tuple2))


# teacher_info = {'name':'111','job':'数学','addr':'上海','age':23}
# for i in teacher_info:
#     print(i)
#
# list1 = ['张三','王五','李四','张三','王五']
# dic = {}
# for i in list1:
#     dic[i] = 1
# print(type(dic.items()))
# print(len(dic))

# i ,j = ('2',3)
# print(type(i),type(j))

# info = {'name': {'大名':'111','小名':'222'},'job':'数学','addr':'上海','age':23}
# if '大名' in info['name']:
#     print('cunzai')


stu1 = {'name':'张三','score':90}
stu2 = {'name':'李四','score':85}
stu3 = {'name':'王五','score':60}
students = [stu1,stu2,stu3]
max_score = 0
score_list = []
for i in students:
    if i['score'] > max_score:
        max_score = i['score']
print(f'全班最高分是{max_score}')

for i in students:
    if i['score'] == max_score:
        print(f'第一名的同学叫{i["name"]}')

for i in students:
    score_list.append(i['score'])
print(f'全班最高成绩是{max(score_list)}')