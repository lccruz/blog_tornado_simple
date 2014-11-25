# -*- coding:utf-8 -*-

import tornado.web

from forms import FormPost
from settings import FACTORY
from dao.Post import Post


class PostView(tornado.web.RequestHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()

    def get(self):
        posts = self.dao_post.get_all()
        self.render("admin_posts_view.html", posts=posts)


class PostInsert(tornado.web.RequestHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()

    def get(self):
        form = FormPost()
        self.render("admin_posts_insert.html", form=form, message='')

    def post(self):
        form = FormPost(self)
        message = ''
        if form.validate():
            post_blog = Post(
                form.titulo.data,
                form.conteudo.data,
            )
            self.dao_post.insert(post_blog)
            message = 'Salvo'
        self.render("admin_posts_insert.html", form=form, message=message)


class PostDelete(tornado.web.RequestHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()

    def get(self, post_id):
        message = "Erro ao excluir"
        if post_id:
            if self.dao_post.delete_um(post_id):
                message = "Excluido"
        self.render("admin_posts_delete.html", message = message)


class PostEdit(tornado.web.RequestHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()

    def get(self, post_id):
        if post_id:
            post = self.dao_post.get_um(post_id)
            if post:
                form = FormPost(obj=post)
        self.render("admin_posts_edit.html", form=form, message='')

    def post(self, post_id):
        form = FormPost(self)
        message = 'Erro'
        if form.validate():
            post_blog = self.dao_post.get_um(form.id.data)
            post_blog.titulo = form.titulo.data
            post_blog.conteudo = form.conteudo.data
            post_blog = self.dao_post.update(post_blog)
            message = 'Editado'
            form = FormPost(obj=post_blog)
        self.render("admin_posts_edit.html", form=form, message=message)
