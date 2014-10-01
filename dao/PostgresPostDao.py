# -*- coding:utf-8 -*-

import psycopg2
from Post import Post


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
                "INSERT INTO post (titulo, conteudo, data, imagem) VALUES (%s, %s, %s, %s)",
                (post.titulo, post.conteudo, post.data, binary)
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
                "UPDATE post SET titulo=%s, conteudo=%s, imagem=%s WHERE id=%s",
                (post.titulo, post.conteudo, binary, post.id)
            )
            consult = self.query.rowcount
            if consult:
                self.conn.commit()
                return post
        else:
            return False

    def get_all(self):
        posts = []
        self.query.execute("SELECT * FROM post")
        postsQuery = self.query.fetchall()
        for post in postsQuery:
            posts.append(Post(post[3], post[2], data=post[1], imagem_binary=post[4], id=post[0]))
        return posts

    def get_um(self, id):
        self.query.execute(
            "SELECT * FROM post WHERE id=(%s)",
            (id, )
        )   
        consult = self.query.fetchone()
        if consult:
            post = Post(consult[3], consult[2], imagem_binary=consult[4], data=consult[1], id=consult[0])
            return post
        return False

    def delete_um(self, id):
        self.query.execute(
            "DELETE FROM post WHERE id=(%s)",
            (id, )
        )
        consult = self.query.rowcount
        if consult:
            self.conn.commit()
            return True
        return False

    def delete_all(self):
        self.query.execute("DELETE FROM post;")
        self.conn.commit()
        return True
