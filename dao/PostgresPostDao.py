# -*- coding:utf-8 -*-

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
            self.query.execute(
                "INSERT INTO post (titulo, conteudo, data) VALUES (%s, %s, %s)",
                (post.titulo, post.conteudo, post.data)
            )
            self.conn.commit()
            return post
        else:
            return False

    def listaAll(self):
        posts = []
        self.query.execute("SELECT * FROM post")
        postsQuery = self.query.fetchall()
        for post in postsQuery:
            posts.append(Post(post[0], post[1]))

    def delete_all(self):
        self.query.execute("DELETE FROM post;")
        self.conn.commit()
        return True
