# -*- coding:utf-8 -*-

import tornado.web

from settings import FACTORY
from util import get_tags

class BlogView(tornado.web.RequestHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()
        self.dao_tag = FACTORY.getTagDao()
        self.tags = self.dao_tag.get_all()
        self.posts = []
        for post in self.dao_post.get_all():
            self.posts.append([post, get_tags(post.id)])

    def get(self):
        posts_only = self.dao_post.get_all()
        self.render("index.html", tags=self.tags, posts=self.posts, posts_only=posts_only)


class BlogViewPost(tornado.web.RequestHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()
        self.dao_tag = FACTORY.getTagDao()
        self.dao_post_tag = FACTORY.getPostTagDao()
        self.tags = self.dao_tag.get_all()
        self.posts_only = self.dao_post.get_all()

    def get(self, post_id):
        if post_id:
            post = self.dao_post.get_um(post_id)
            if post:
                self.render(
                    "blog_post.html",
                    tags=self.tags,
                    posts=[[post, get_tags(post.id)],],
                    posts_only=self.posts_only,
                )

        self.render(
            "blog_post.html",
            tags=self.tags,
            posts=[],
            posts_only=self.posts_only,
        )


class BlogViewTag(tornado.web.RequestHandler):

    def initialize(self):
        self.dao_post = FACTORY.getPostDao()
        self.dao_tag = FACTORY.getTagDao()
        self.dao_post_tag = FACTORY.getPostTagDao()
        self.tags = self.dao_tag.get_all()
        self.posts_only = self.dao_post.get_all()

    def get(self, tag_id):
        if tag_id:
            tag = self.dao_tag.get_um(tag_id)
            if tag:
                list_post_tags = self.dao_post_tag.get_all_posts_tag(tag.id)
                self.render(
                    "blog_tag.html",
                    tagnome=tag.nome,
                    tags=self.tags,
                    posts= list_post_tags,
                    posts_only=self.posts_only,
                    total=len(list_post_tags),
                )

        self.render(
            "blog_tag.html",
            tags=self.tags,
            posts=[],
            posts_only=self.posts_only,
            tagnome="Error",
            total=0,
        )


class Contato(tornado.web.RequestHandler):
    def initialize(self):
        self.dao_post = FACTORY.getPostDao()
        self.dao_tag = FACTORY.getTagDao()

    def get(self):
        posts_only = self.dao_post.get_all()
        self.render("blog_contato.html", tags=self.dao_tag.get_all(), posts_only=posts_only)


class Busca(tornado.web.RequestHandler):
    def initialize(self):
        self.dao_post = FACTORY.getPostDao()
        self.dao_tag = FACTORY.getTagDao()

    def get(self):
        dado  = self.get_argument('search')
        posts_only = self.dao_post.get_all()
        posts = self.dao_post.search(dado)
        self.render("blog_busca.html", tags=self.dao_tag.get_all(), posts_only=posts_only, posts=posts)
