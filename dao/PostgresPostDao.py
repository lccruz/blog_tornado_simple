# -*- coding:utf-8 -*-

import psycopg2
from Post import Post
from utils import delete_arquivo


class PostgresPostDao(object):
    """ Class PostgresPostDao
    """
    def __init__(self, conn, cur):
        # conexao db
        self.conn = conn
        self.query = cur()

    def insert(self, post):
        if isinstance(post, Post):
            binary = psycopg2.Binary(post.imagem_binary)
            self.query.execute(
                "INSERT INTO post (titulo, conteudo, data, imagem, arquivopath) VALUES (%s, %s, %s, %s, %s)",
                (post.titulo, post.conteudo, post.data, binary, post.arquivopath)
            )
            self.conn.commit()
            self.query.execute("SELECT MAX(id) FROM post")
            consult = self.query.fetchone()
            post.id = consult[0]
            return post
        else:
            return False

    def update(self, post):
        if isinstance(post, Post):
            binary = psycopg2.Binary(post.imagem_binary)
            self.query.execute(
                "UPDATE post SET titulo=%s, conteudo=%s, imagem=%s, arquivopath=%s WHERE id=%s",
                (post.titulo, post.conteudo, binary, post.arquivopath, post.id)
            )
            consult = self.query.rowcount
            if consult:
                self.conn.commit()
                return post
        else:
            return False

    def get_all(self):
        posts = []
        self.query.execute("SELECT * FROM post ORDER BY data DESC")
        postsQuery = self.query.fetchall()
        for post in postsQuery:
            posts.append(Post(post[3], post[2], data=post[1], imagem_binary=post[4], arquivopath=post[5], id=post[0]))
        return posts

    def get_um(self, id):
        self.query.execute(
            "SELECT * FROM post WHERE id=(%s)",
            (id, )
        )   
        consult = self.query.fetchone()
        if consult:
            post = Post(consult[3], consult[2], imagem_binary=consult[4], data=consult[1], arquivopath=consult[5], id=consult[0])
            return post
        return False

    def delete_um(self, id):
        post = self.get_um(id)
        if post:
            self.query.execute(
                "DELETE FROM post WHERE id=(%s)",
                (id, )
            )
            consult = self.query.rowcount
            if consult:
                delete_arquivo(post.arquivopath)
                self.conn.commit()
                return True
        return False

    def delete_all(self):
        self.query.execute("DELETE FROM post;")
        self.conn.commit()
        return True

    def search(self, term):
        posts = []
        term= term.replace('=', '==').replace('%', '=%').replace('_', '=_')
        sql= "SELECT * FROM post WHERE titulo LIKE %(like)s ESCAPE '='"
        self.query.execute(sql, dict(like = '%'+term+'%'))
        postsQuery = self.query.fetchall()
        for post in postsQuery:
            posts.append(Post(post[3], post[2], data=post[1], imagem_binary=post[4], arquivopath=post[5], id=post[0]))
        return posts
