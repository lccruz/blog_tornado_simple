# -*- coding:utf-8 -*-

import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import tornado.httpserver

from tornado.options import define, options
from forms import FormTag
from settings import FACTORY
from tag_controler import *
from post_controler import *
from blog_controler import BlogView
from blog_controler import BlogViewPost
from blog_controler import BlogViewTag

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", BlogView),
            (r"/post/(.*)", BlogViewPost),
            (r"/tag/(.*)", BlogViewTag),
            (r"/tags/", TagView),
            (r"/admin/", PostView),
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
            xsrf_cookies=False,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
