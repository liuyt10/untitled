from 学员管理系统.student import Student


class FileOperate:
    file_path = r'E:\project\untitled\学员管理系统\students.txt'

    @classmethod
    def read(cls):
        # 读取文件
        # 读到的内容需要以什么样的数据结构进行存储，才方便后续处理
        # {id1:stu1,id2:stu2,id3:stu3}
        # 以字典作为读取到的数据存储形式，字典的key表示每个学员的id，字典的value表示每个学员对象
        stu_dict = {}
        with open(cls.file_path, mode='r', encoding='utf-8') as f:
            ret = f.readlines()
            for i in ret:
                i = i.strip()
                line_split = i.split(',')
                id = line_split[0]
                name = line_split[1]
                phone = line_split[2]
                score = line_split[3]
                wx = line_split[4]
                qq = line_split[5]
                stu = Student(id, name, phone, score, wx, qq)
                stu_dict[int(id)] = stu
        return stu_dict

    @classmethod
    def write(cls, stu_dict):
        with open(cls.file_path, mode='w', encoding='utf-8') as f:
            for id in stu_dict:
                f.write(str(stu_dict[id]))
                f.write('\n')

# stu_dict = FileOperate().read()
# FileOperate().write(stu_dict)
