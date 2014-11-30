# -*- coding:utf-8 -*-

import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import tornado.httpserver

from tag_controler import TagView
from tag_controler import TagInsert
from tag_controler import TagDelete
from tag_controler import TagEdit
from post_controler import PostView
from post_controler import PostInsert
from post_controler import PostDelete
from post_controler import PostEdit
from blog_controler import BlogView
from blog_controler import BlogViewPost
from blog_controler import Contato
from blog_controler import Busca
from blog_controler import BlogViewTag
from login_controler import LoginHandler
from login_controler import LogoutHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", BlogView),
            (r"/login", LoginHandler),
            (r"/tag/(.*)", BlogViewTag),
            (r"/contato", Contato),
            (r"/busca/", Busca),
            (r"/logout", LogoutHandler),
            (r"/post/(.*)", BlogViewPost),
            (r"/tags/", TagView),
            (r"/tagsinsert/", TagInsert),
            (r"/tag_delete/(\w+)", TagDelete),
            (r"/tag_edit/(.*)", TagEdit),
            (r"/posts/", PostView),
            (r"/postsinsert/", PostInsert),
            (r"/post_delete/(\w+)", PostDelete),
            (r"/post_edit/(.*)", PostEdit),
        ]
        settings = dict(
            cookie_secret="V3f23B2YRDxQIzpftlGTrLqbKsfEN6J1o0L8ulA",
            debug=True,
            autoreload=True,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            login_url="/login",
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
