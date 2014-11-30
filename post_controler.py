# -*- coding:utf-8 -*-

import os
import string
import random
import tornado.web

from forms import FormPost
from settings import FACTORY
from util import get_tags
from utils import read_arquivo
from utils import save_arquivo
from utils import delete_arquivo
from utils import rename_arquivo
from dao.Post import Post
from base_controler import BaseHandler


class PostView(BaseHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()

    @tornado.web.authenticated
    def get(self):
        posts = self.dao_post.get_all()
        self.render("admin_posts_view.html", posts=posts)


class PostInsert(BaseHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()
        self.dao_post_tag = FACTORY.getPostTagDao()

    @tornado.web.authenticated
    def get(self):
        form = FormPost()
        self.render("admin_posts_insert.html", form=form, message='')
    
    @tornado.web.authenticated
    def post(self):
        form = FormPost(self)
        message = ''
        imagem_binary = ''
        final_filename=''
        arquivo_filename = ''
        if form.validate():
            if self.request.files.has_key('imagem'):
                imagem = self.request.files['imagem'][0]
                imagem_filename = imagem['filename']
                extension = os.path.splitext(imagem_filename)[1]
                if form.validate_imagem(extension):
                    fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
                    final_filename= fname + extension
                    save_arquivo(imagem['body'], final_filename)
                    imagem_binary = read_arquivo(final_filename)
                else:
                    form.imagem.errors = ['Somente arquivo jpg',]
                    self.render("admin_posts_insert.html", form=form, message=message)
     
            if self.request.files.has_key('arquivo'):
                arquivo = self.request.files['arquivo'][0]
                arquivo_filename = arquivo['filename']
                save_arquivo(arquivo['body'], arquivo_filename)
            post_blog = Post(
                form.titulo.data,
                form.conteudo.data,
                imagem_binary = imagem_binary,
                arquivopath = arquivo_filename,
            )
            self.dao_post.insert(post_blog)
            rename_arquivo(final_filename,post_blog.id)
            message = 'Salvo'
            self.dao_post_tag.insert(post_blog.id, form.tags.data)
        self.render("admin_posts_insert.html", form=form, message=message)


class PostDelete(BaseHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()

    @tornado.web.authenticated
    def get(self, post_id):
        message = "Erro ao excluir"
        if post_id:
            post = self.dao_post.get_um(post_id)
            if self.dao_post.delete_um(post.id):
                delete_arquivo(post_id+'.jpg',False)
                delete_arquivo(post.arquivopath,False)
                message = "Excluido"
        self.render("admin_posts_delete.html", message = message)


class PostEdit(BaseHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()
        self.dao_post_tag = FACTORY.getPostTagDao()

    @tornado.web.authenticated
    def get(self, post_id):
        imagem = ''
        arquivo = ''
        if post_id:
            post = self.dao_post.get_um(post_id)
            if post:
                form = FormPost(obj=post)
                if post.imagem_binary:
                    imagem = "%s.jpg" % (post_id)
                if post.arquivopath:
                    arquivo = post.arquivopath
        self.render(
            "admin_posts_edit.html",
            form=form,
            message='',
            tags_atual = get_tags(post.id),
            imagem=imagem,
            arquivo=arquivo,
        )

    @tornado.web.authenticated
    def post(self, post_id):
        form = FormPost(self)
        message = 'Erro'
        imagem_binary = ''
        imagem = ''
        arquivo_filename=''
        arquivo = ''
        final_filename=''
        if form.validate():
            post_blog = self.dao_post.get_um(form.id.data)
            if self.request.files.has_key('imagem'):
                imagem = self.request.files['imagem'][0]
                imagem_filename = imagem['filename']
                extension = os.path.splitext(imagem_filename)[1]
                if form.validate_imagem(extension):
                    final_filename= "%s%s" % (post_blog.id, extension)
                    save_arquivo(imagem['body'], final_filename)
                    imagem_binary = read_arquivo(final_filename)
                else:
                    form.imagem.errors = ['Somente arquivo jpg',]
                    self.render("admin_posts_edit.html", form=form, message=message)
            if self.request.files.has_key('arquivo'):
                arquivo = self.request.files['arquivo'][0]
                arquivo_filename = arquivo['filename']
                delete_arquivo(post_blog.arquivopath,False)
                save_arquivo(arquivo['body'], arquivo_filename)
            post_blog.titulo = form.titulo.data
            post_blog.conteudo = form.conteudo.data
            if imagem_binary:
                post_blog.imagem_binary = imagem_binary
            if arquivo:
                post_blog.arquivopath = arquivo_filename
            post_blog = self.dao_post.update(post_blog)
            if post_blog.imagem_binary:
                imagem="%s.jpg" % (post_id)
            message = 'Editado'
            if form.tags.data:
                for tag in self.dao_post_tag.get_all_tags_post(post_blog.id):
                    self.dao_post_tag.delete_um(post_blog.id, tag.id)
                self.dao_post_tag.insert(post_blog.id, form.tags.data)
            form = FormPost(obj=post_blog)
        self.render(
            "admin_posts_edit.html",
            form=form,
            message=message,
            tags_atual = get_tags(post_blog.id),
            imagem=imagem,
            arquivo=arquivo_filename,
        )
