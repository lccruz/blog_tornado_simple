# -*- coding:utf-8 -*-

from Tag import Tag


class PostgresTagDao(object):
    """ Class PostgresTagDao
    """
    def __init__(self, conn, cur):
        # conexao db
        self.conn = conn
        self.query = cur()

    def insert(self, tag):
        if isinstance(tag, Tag):
            self.query.execute(
                "INSERT INTO tag (nome) VALUES (%s)",
                (tag.nome,)
            )
            self.conn.commit()
            return tag
        else:
            return False

    def listaAll(self):
        tags = []
        self.query.execute("SELECT * FROM tags")
        tagsQuery = self.query.fetchall()
        for tag in tagsQuery:
            tags.append(Tag(tag[0], tag[1]))

    def delete_all(self):
        self.query.execute("DELETE FROM tag;")
        self.conn.commit()
        return True
