# -*- coding:utf-8 -*-
from api.base_api import BaseBuyerApi


class SubmitCommet(BaseBuyerApi):
    def __init__(self):
        super().__init__()
        self.url = f'{self.host}/members/comments'
