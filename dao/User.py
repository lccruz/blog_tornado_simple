# -*- coding:utf-8 -*-

from utils import convert_md5


class User(object):
    """
       Classe Usuario
    """
    def __init__(self, nome, email, password, id=id):
        self.nome = nome
        self.email = email
        self.password = convert_md5(password)
        self.id = id
