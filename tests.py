# -*- coding: utf-8 -*-

import unittest
from utils import convert_md5
from settings import FACTORY
from dao.Tag import Tag
from dao.User import User


class TestTag(unittest.TestCase):
    def setUp(self):
        self.dao_tag = FACTORY.getTagDao()
        self.dao_user = FACTORY.getUserDao()

    def test_convert_md5(self):
        password = convert_md5('teste')
        self.assertEqual(password, '698dc19d489c4e4db73e28a713eab07b')
        password = convert_md5('Python')
        self.assertEqual(password, 'a7f5f35426b927411fc9231b56382173')
        password = convert_md5('Luciano')
        self.assertNotEqual(password, 'Luciano')

    def test_insert_tag(self):
        tag = Tag('python')
        new_tag = self.dao_tag.insert(tag)
        self.assertEqual(tag.nome, new_tag.nome)
        new_tag = self.dao_tag.insert('a')
        self.assertFalse(new_tag)
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

if __name__ == '__main__':
    unittest.main()
