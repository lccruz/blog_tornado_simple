# -*- coding:utf-8 -*-

import tornado.web

from forms import FormTag
from settings import FACTORY
from dao.Tag import Tag
from base_controler import BaseHandler


class TagView(BaseHandler):

    def initialize(self):
        self.dao_tag = FACTORY.getTagDao()

    @tornado.web.authenticated
    def get(self):
        tags = self.dao_tag.get_all()
        self.render("admin_tags_view.html", tags=tags)


class TagInsert(BaseHandler):

    def initialize(self):
        self.dao_tag = FACTORY.getTagDao()

    @tornado.web.authenticated
    def get(self):
        form = FormTag()
        self.render("admin_tags_insert.html", form=form, message='')

    @tornado.web.authenticated
    def post(self):
        form = FormTag(self)
        message = ''
        if form.validate():
            tag = Tag(form.nome.data)
            self.dao_tag.insert(tag)
            message = 'Salvo'
        self.render("admin_tags_insert.html", form=form, message=message)


class TagDelete(BaseHandler):

    def initialize(self):
        self.dao_tag = FACTORY.getTagDao()

    @tornado.web.authenticated
    def get(self, tag_id):
        message = "Erro ao excluir"
        if tag_id:
            if self.dao_tag.delete_um(tag_id):
                message = "Excluido"
        self.render("admin_tags_delete.html", message = message)


class TagEdit(BaseHandler):

    def initialize(self):
        self.dao_tag = FACTORY.getTagDao()

    @tornado.web.authenticated
    def get(self, tag_id):
        if tag_id:
            tag = self.dao_tag.get_um(tag_id)
            if tag:
                form = FormTag(obj=tag)
        self.render("admin_tags_edit.html", form=form, message='')

    @tornado.web.authenticated
    def post(self, tag_id):
        form = FormTag(self)
        message = 'Erro'
        if form.validate():
            tag = self.dao_tag.get_um(form.id.data)
            tag.nome = form.nome.data
            tag = self.dao_tag.update(tag)
            message = 'Editado'
            form = FormTag(obj=tag)
        self.render("admin_tags_edit.html", form=form, message=message)
