import os.path

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

from tornado.options import define, options

define("port", default=8000, help="run on the port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        one = 'hello,world!!!'
        self.render('index.html', one=one)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', MainHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "template")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
