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
from dao.Tag import Tag
from tag_controler import *

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", Blog),
            (r"/tags/", TagView),
            (r"/tagsinsert/", TagInsert),
            (r"/tag_delete/(\w+)", TagDelete),
            (r"/tag_edit/(.*)", TagEdit),
        ]
        settings = dict(
            cookie_secret="V3f23B2YRDxQIzpftlGTrLqbKsfEN6J1o0L8ulA",
            debug=True,
            autoreload=True,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class Blog(tornado.web.RequestHandler):
    def get(self):
        form = FormTag()
        self.render("index.html", form=form)

    def post(self):
        form = FormTag(self)
        if form.validate():
            self.write("<h2>OK</h2>")
        self.render("index.html", form=form)


def main():
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
