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
            self.query.execute("SELECT MAX(id) FROM tag")
            consult = self.query.fetchone()
            tag.id = consult[0]
            return tag
        else:
            return False

    def update(self, tag):
        if isinstance(tag, Tag):
            self.query.execute(
                "UPDATE tag SET nome=%s WHERE id=%s",
                (tag.nome, tag.id)
            )
            consult = self.query.rowcount
            if consult:
                self.conn.commit()
                return tag
        else:
            return False

    def get_all(self):
        tags = []
        self.query.execute("SELECT * FROM tag")
        tagsQuery = self.query.fetchall()
        for tag in tagsQuery:
            tags.append(Tag(tag[1], id=tag[0]))
        return tags

    def get_um(self, id):
        self.query.execute(
            "SELECT * FROM tag WHERE id=(%s)",
            (id, )
        )
        consult = self.query.fetchone()
        if consult:
            tag = Tag(consult[1], id=consult[0])
            return tag
        return False

    def delete_um(self, id):
        self.query.execute(
            "DELETE FROM tag WHERE id=(%s)",
            (id, )
        )
        consult = self.query.rowcount
        if consult:
            self.conn.commit()
            return True
        return False

    def delete_all(self):
        self.query.execute("DELETE FROM tag;")
        self.conn.commit()
        return True
