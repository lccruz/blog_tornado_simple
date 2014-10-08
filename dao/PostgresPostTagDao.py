# -*- coding:utf-8 -*-

from Post import Post
from Tag import Tag


class PostgresPostTagDao(object):
    """ Class PostgresPostTagDao
    """
    def __init__(self, conn, cur):
        # conexao db
        self.conn = conn
        self.query = cur()

    def insert(self, post_id, tags_id=[]):
        self.query.execute(
            "SELECT * FROM post WHERE id=(%s)",
            (post_id, )
        )
        consult = self.query.fetchone()
        if consult:
            for tag_id in tags_id:
                self.query.execute(
                    "SELECT * FROM tag WHERE id=(%s)",
                    (tag_id, )
                )
                consult = self.query.fetchone()
                if consult:
                    self.query.execute(
                        "INSERT INTO post_tag (post_id, tag_id) VALUES (%s, %s)",
                        (post_id, tag_id)
                    )
                    self.conn.commit()
            return True
        else:
            return False

    def get_all_posts_tag(self, id):
        """Retornar uma lista com todos os post de uma tag
        """
        posts = []
        self.query.execute(
            "SELECT * FROM post_tag WHERE tag_id=(%s)",
            (id, )
        )
        postQuery = self.query.fetchall()
        for post in postQuery:
            self.query.execute(
                "SELECT * FROM post WHERE id=(%s)",
                (post[0], )
            )
            consult = self.query.fetchone()
            if consult:
                posts.append(Post(consult[3], consult[2], data=consult[1], imagem_binary=consult[4], id=consult[0]))
        return posts

    def get_all_tags_post(self, id):
        """Retorna todas as tag de um post
        """
        tags = []
        self.query.execute(
            "SELECT * FROM post_tag WHERE post_id=(%s)",
            (id, )
        )
        tagQuery = self.query.fetchall()
        for tag in tagQuery:
            self.query.execute(
                "SELECT * FROM tag WHERE id=(%s)",
                (tag[1], )
            )
            consult = self.query.fetchone()
            if consult:
                tags.append(Tag(consult[1], id=consult[0]))
        return tags

    def delete_um(self, post_id, tag_id):
        """Delete uma listacao post|tag
        """
        self.query.execute(
            "SELECT * FROM post WHERE id=(%s)",
            (post_id, )
        )
        consult = self.query.fetchone()
        if consult:
            self.query.execute(
                "SELECT * FROM tag WHERE id=(%s)",
                (tag_id, )
            )
            consult = self.query.fetchone()
            if consult:
                self.query.execute(
                    "DELETE FROM post_tag WHERE post_id=(%s) and tag_id=(%s)",
                    (post_id, tag_id)
                )
                consult = self.query.rowcount
                if consult:
                    self.conn.commit()
                    return True
        return False
