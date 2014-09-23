# -*- coding:utf-8 -*-

import psycopg2

from PostgresTagDao import PostgresTagDao
from PostgresUserDao import PostgresUserDao


class PostgresDaoFactory(object):
    """ PostgresDaoFactory
    """
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                user='postgres',
                database='blog_demo',
                password='root',
                port=5432,
            )
            self.cur = self.conn.cursor

        except:
            print "Erro ao se conectar a base de dados!"
            if self.conn:
                self.conn.close()

    def __del__(self):
        print "Conexão finalizada!"
        del self

    def getPostDao(self):
        pass

    def getUserDao(self):
        return PostgresUserDao(self.conn, self.cur)

    def getTagDao(self):
        return PostgresTagDao(self.conn, self.cur)
