import requests_study
# sum = 0
# i =1
# while i<=100:
#     if i%15==0:
#         sum += i
#     i += 1
# print(sum)

# i = 0
# while i < 5:
#     i += 1
#     if i==3:
#         print('有虫子')
#         continue
#     print(f'吃了第{i}个苹果')

# ss = {'12':34,'10':38}
# ss.__reversed__()
# print(ss)


l = ['Hello', 'World', 18, 'Apple', None]
# l_new = []
# for i in l:
#     if type(i) == str:
#         i = i.lower()
#     l_new.append(i)
#
# print(l_new)
# print(type(l[4]))

for i in range(len(l)):
    if isinstance(l[i], str):
        l[i] = l[i].lower()


def add(a, b) -> int:  # 参数类型声明，增加可读性，增加代码的编辑效率
    return (a + b)


def find_last_only_one(s):
    for i in s[::-1]:
        if s.count(i) == 1:
            index = s.find(i)
            return i, index


if __name__ == '__main__':
    # add('23', 'dhfs')
    # c1 = find_last_only_one('fdahionbfjnvfdjjl')
    # c2 = find_last_only_one('dhahrtjstytjytj')
    # c = add(c1, c2)
    # print(c1)
    # print(c2)
    # print(c1[0] + c2[0])
    l = [1,2,3]
    print(l.insert(2,5))
    print(l)

