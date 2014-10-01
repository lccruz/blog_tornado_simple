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
            self.query.execute("SELECT MAX(id) FROM usuario")
            consult = self.query.fetchone()
            user.id = consult[0]
            return user
        else:
            return False

    def update(self, user):
        if isinstance(user, User):
            self.query.execute(
                "UPDATE usuario SET nome=%s, email=%s, password=%s WHERE id=%s",
                (user.nome, user.email, user.password, user.id)
            )   
            consult = self.query.rowcount
            if consult:
                self.conn.commit()
                return user
        else:
            return False

    def get_all(self):
        users = []
        self.query.execute("SELECT * FROM usuario")
        usersQuery = self.query.fetchall()
        for user in usersQuery:
            users.append(User(user[1], user[2], user[3], id=user[0]))
        return users

    def get_um(self, id):
        self.query.execute(
            "SELECT * FROM usuario WHERE id=(%s)",
            (id, )
        )   
        consult = self.query.fetchone()
        if consult:
            user = User(consult[1], consult[2], consult[3], id=consult[0])
            return user
        return False

    def delete_um(self, id):
        self.query.execute(
            "DELETE FROM usuario WHERE id=(%s)",
            (id, )
        )   
        consult = self.query.rowcount
        if consult:
            self.conn.commit()
            return True
        return False

    def delete_all(self):
        self.query.execute("DELETE FROM usuario;")
        self.conn.commit()
        return True
