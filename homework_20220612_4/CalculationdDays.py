# _*_ coding: utf-8 _*_


def CikeDay(mouth, day):  # 判断月份和日期是否正确
    if mouth > 12 or mouth <= 0:
        print('您输入的月份不对')
        return 0

    else:
        if day > mouth_days[mouth -1]:
            print('您输入的天数超过了当月的天数')
            return 0
        else:
            return 1


mouth_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print('您现在正在运行的是日期天数的查询程序....')
while True:
    input_days = input('请输入你要查询的时间,输入格式为(2022.5.6),退出请输入"q"或"Q":')
    sum_days = 0
    if input_days.lower() == 'q':
        print('感谢您的使用，期待您的下次光临')
        break
    else:
        try:
            input_year, input_mouth, input_day = input_days.split('.')
            input_year = int(input_year)
            input_mouth = int(input_mouth)
            input_day = int(input_day)
            if input_year % 4 == 0:
                if input_year % 100 == 0:
                    if input_year % 400 == 0:
                        mouth_days[1] = 29
                    else:
                        pass
                else:
                    mouth_days[1] = 29

            if CikeDay(input_mouth, input_day):
                for i in range(len(mouth_days)):
                    if i < input_mouth - 1:
                        sum_days += mouth_days[i]
                sum_days += input_day
                print(f'{input_year}年{input_mouth}月{input_day}日是{input_year}年的第{sum_days}天')
        except Exception as e:
            print('您输入的日期格式不正确，请重新输入')

