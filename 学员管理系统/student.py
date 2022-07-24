class Student:
    def __init__(self, id, name, phone, score=0, wx='', qq=''):
        self.id = id
        self.name = name
        self.phone = phone
        self.wx = wx
        self.qq = qq
        self.score = score

    def __str__(self):
        return f'{self.id},{self.name},{self.phone},{self.score},{self.wx},{self.qq}'
