# user ={'username':'liuyuting','age':25,'job':'tester'}
# tuple1 = ('xinxi','keji','jishu','fazhan')
#
# print('判断user是否是字典类型：{}'.format(isinstance(user,dict)))
# print('判断user是否是字典类型：{}'.format(isinstance(tuple1,dict)))

name = input('请输入你的姓名：')
year = input('请输入你入职的年份：')
month = input('请输入你入职的月份：')
day = input('请输入你入职的日期：')
department = input('请输入你入职的部门：')
job = input('请输入你入职的岗位：：')

# print(f'兹证明{name}自{year}年{month}月{day}日入职，在我公司担任{department}部门{job}岗位')
# print('兹证明{}自{}年{}月{}日入职，在我公司担任{}部门{}岗位'.format(name,year,month,day,department,job))
print(f'兹证明{name}自{year}年{month}月{day}日入职。'
      f'在我公司担任{department}部门{job}岗位.兹证明{name}自{year}年{month}月{day}日入职。')
      # format(tester_name=name,start_year=year,start_month=month,terster=job,start_day=day,?
#              test_department=department))
# print(f'{user}自从数据')
# print('数据','信息')
# a,b,c = 10,20,30
# print('##########'  + f'{a>b and b>c}')  #F
# print(a>b and b>c or a<c)  # F and F or T
# print('##########'  + f'{a<b and b>c}')
# print(a<b and b>c or a<c)  # T and F or T
# print('##########'  + f'{a<b and b>c}')
# print(a<b and b>c or a>c)  # T and F or F
# print('##########'  + f'{a<b or b<c}')
# print(a<b or b<c and a>c)  # T or T and F
# print(True or False )
# print(True or False and False)  # T or T and F,先算and，后算or
