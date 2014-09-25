# -*- coding:utf-8 -*-

import datetime


class Post(object):
    """
       Classe Post
    """
    def __init__(self, titulo, conteudo, id=0):
        self.titulo = titulo
        self.conteudo = conteudo
        self.data = datetime.datetime.now()
        self.id = id
