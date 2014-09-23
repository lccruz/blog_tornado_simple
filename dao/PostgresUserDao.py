# -*- coding:utf-8 -*-

from User import User


class PostgresUserDao(object):
    """ Class PostgresUserDao
    """
    def __init__(self, conn, cur):
        # conexao db
        self.conn = conn
        self.query = cur()

    def insert(self, user):
        if isinstance(user, User):
            self.query.execute(
                "INSERT INTO usuario (nome, email, password) VALUES (%s, %s, %s)",
                (user.nome, user.email, user.password,)
            )
            self.conn.commit()
            return user
        else:
            return False

    def listaAll(self):
        tags = []
        self.query.execute("SELECT * FROM usuario")
        tagsQuery = self.query.fetchall()
        for tag in tagsQuery:
            tags.append(Tag(tag[0], tag[1]))

    def delete_all(self):
        self.query.execute("DELETE FROM usuario;")
        self.conn.commit()
        return True
