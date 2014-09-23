# -*- coding:utf-8 -*-

import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import tornado.httpserver

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", Blog),
        ]
        settings = dict(
            cookie_secret="V3f23B2YRDxQIzpftlGTrLqbKsfEN6J1o0L8ulA",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class Blog(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=[])


def main():
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
