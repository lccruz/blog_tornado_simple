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
            self.query.execute("SELECT MAX(id) FROM post")
            consult = self.query.fetchone()
            post.id = consult[0]
            return post
        else:
            return False

    def update(self, post):
        if isinstance(post, Post):
            self.query.execute(
                "UPDATE post SET titulo=%s, conteudo=%s WHERE id=%s",
                (post.titulo, post.conteudo, post.id)
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
            posts.append(Post(post[0], id=post[1]))
        return posts

    def get_um(self, id):
        self.query.execute(
            "SELECT * FROM post WHERE id=(%s)",
            (id, )
        )   
        consult = self.query.fetchone()
        if consult:
            post = Post(consult[1], consult[2], id=consult[0], data=consult[3])
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
