# -*- coding: utf-8 -*-

import unittest
from utils import convert_md5
from settings import FACTORY
from dao.Tag import Tag
from dao.User import User
from dao.Post import Post


class TestTag(unittest.TestCase):
    def setUp(self):
        self.dao_tag = FACTORY.getTagDao()
        self.dao_tag.delete_all()
        self.dao_user = FACTORY.getUserDao()
        self.dao_post = FACTORY.getPostDao()

    def test_convert_md5(self):
        password = convert_md5('teste')
        self.assertEqual(password, '698dc19d489c4e4db73e28a713eab07b')
        password = convert_md5('Python')
        self.assertEqual(password, 'a7f5f35426b927411fc9231b56382173')
        password = convert_md5('Luciano')
        self.assertNotEqual(password, 'Luciano')

    def test_tag(self):
        # insert
        tag = Tag('python')
        new_tag = self.dao_tag.insert(tag)
        self.assertEqual(tag.nome, new_tag.nome)
        new_tag2 = self.dao_tag.insert('a')
        self.assertFalse(new_tag2)

        # update
        tag.nome = "Python"
        new_tag = self.dao_tag.update(tag)
        self.assertEqual(tag.nome, new_tag.nome)

        # get one
        id = new_tag.id
        new_tag = self.dao_tag.get_um(id)
        self.assertEqual(id, new_tag.id)

        new_tag2 = self.dao_tag.get_um(10000)
        self.assertFalse(new_tag2)

        # get all
        tag = Tag('python2')
        new_tag = self.dao_tag.insert(tag)
        cont = self.dao_tag.get_all()
        self.assertEqual(2, len(cont))

        # delete um
        self.assertTrue(self.dao_tag.delete_um(new_tag.id))

        # delete all
        self.assertTrue(self.dao_tag.delete_all())

    def test_insert_user(self):
        user = User(
            "Luciano",
            "luciano@lccruz.net",
            "a7f5f35426b927411fc9231b56382173",
        )
        new_user = self.dao_user.insert(user)
        self.assertEqual(user.nome, new_user.nome)
        self.assertEqual(user.email, new_user.email)
        self.assertEqual(user.password, new_user.password)
        new_user = self.dao_user.insert('Luciano')
        self.assertFalse(new_user)
        self.assertTrue(self.dao_user.delete_all())

    def test_insert_post(self):
        post= Post('Post1', 'Conteudo')
        new_post = self.dao_post.insert(post)
        self.assertEqual(post.titulo, new_post.titulo)
        self.assertEqual(post.conteudo, new_post.conteudo)
        new_post = self.dao_post.insert('Post')
        self.assertFalse(new_post)
        self.assertTrue(self.dao_post.delete_all())


if __name__ == '__main__':
    unittest.main()
