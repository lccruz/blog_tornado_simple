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
        self.dao_post = FACTORY.getPostDao()
        self.assertTrue(self.dao_post.delete_all())
        self.dao_user = FACTORY.getUserDao()
        self.assertTrue(self.dao_user.delete_all())

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

    def test_insert_post(self):
        # insert
        imagem = open('static/img/python.png','rb')
        imagem = imagem.read()
        post= Post('Post1', 'Conteudo', imagem_binary = imagem)
        new_post = self.dao_post.insert(post)
        self.assertEqual(post.titulo, new_post.titulo)
        self.assertEqual(post.conteudo, new_post.conteudo)
        self.assertEqual(len(post.imagem_binary), len(new_post.imagem_binary))
        new_post = self.dao_post.insert('Post')
        self.assertFalse(new_post)

        # update
        post.titulo = "Post Python"
        post.conteudo = "Conteudo Python"
        new_post = self.dao_post.update(post)
        self.assertEqual(post.titulo, new_post.titulo)
        self.assertEqual(post.conteudo, new_post.conteudo)

        # get one
        id = new_post.id
        new_post = self.dao_post.get_um(id)
        self.assertEqual(id, new_post.id)

        new_post2 = self.dao_post.get_um(10000)
        self.assertFalse(new_post2)

        # get all
        cont = self.dao_post.get_all()
        self.assertEqual(1, len(cont))

        # delete um
        self.assertTrue(self.dao_post.delete_um(new_post.id))

        # delete all
        self.assertTrue(self.dao_post.delete_all())

    def test_insert_user(self):
        # insert
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

        # update
        user.nome = "Luciano Camargo Cruz"
        new_user = self.dao_user.update(user)
        self.assertEqual(user.nome, new_user.nome)

        # get one
        id = user.id
        new_user = self.dao_user.get_um(id)
        self.assertEqual(id, new_user.id)

        new_user2 = self.dao_user.get_um(10000)
        self.assertFalse(new_user2)

        # get all
        cont = self.dao_user.get_all()
        self.assertEqual(1, len(cont))

        # delete um
        self.assertTrue(self.dao_user.delete_um(new_user.id))

        # delete all
        self.assertTrue(self.dao_user.delete_all())


if __name__ == '__main__':
    unittest.main()
