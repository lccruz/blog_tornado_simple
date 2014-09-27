# -*- coding:utf-8 -*-

import datetime


class Post(object):
    """
       Classe Post
    """
    def __init__(self, titulo, conteudo, id=0, data=None):
        self.titulo = titulo
        self.conteudo = conteudo
        if data:
            self.data = data
        else:
            self.data = datetime.datetime.now()
        self.id = id
