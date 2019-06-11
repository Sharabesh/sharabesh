import os
# Modules to run webserver
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
from models import *
from mailer import *
import json
from remainder import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/index.html", failure=0)


# Test to store cookie values in my DB
class CookieHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', ' PUT, DELETE, OPTIONS')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


    def post(self, *args, **kwargs):
        retrieved_cookie = self.get_argument("cookie")
        print(retrieved_cookie)
        q = Cookies.insert(
            cookie_value = retrieved_cookie
        )
        q.execute()


class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/contact.html", failure=0, message="")


class NotFoundHandler(tornado.web.ErrorHandler, tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.set_status(404)
        self.render("static/html/404.html")

# class StaticNotFoundHandler(tornado.web.StaticFileHandler):
#     def write_error(self, status_code, *args, **kwargs):
#         # custom 404 page
#         print("I AM HERE")
#         print("STATUS CODE IS ",status_code)
#         self.render('static/html/404.html')


class ResponseHandler(tornado.web.RequestHandler):
    async def post(self):
        name = self.get_body_argument("name")
        from_addr = self.get_body_argument("email")
        phone = self.get_body_argument("phone")
        message = self.get_body_argument("message")
        captcha_repsonse = self.get_body_argument("g-recaptcha-response")

        resp, msg = await issue_message(name, from_addr, phone, message, captcha_repsonse)
        self.write(json.dumps({"success": int(resp), "message": msg}))


class EducationHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/new_education.html")


# class KernalHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("static/html/Kernels.html")


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "compress_response": True,
    'default_handler_class': NotFoundHandler,
    'default_handler_args': dict(status_code=404),
    'xheaders': True,
    'protocol': 'https'
}


def make_app():
    debug = not bool(os.environ.get("PRODUCTION"))
    return tornado.web.Application([
        (r"/static/(.*)", tornado.web.StaticFileHandler,
         dict(path=settings["static_path"])),
        (r"/", MainHandler),
        (r"/contact", ContactHandler),
        (r"/education", EducationHandler),
        (r"/response", ResponseHandler),
        (r"/cookie", CookieHandler),
        (r"/remainder", RemainderHandler),
        (r"/socket", WebSocketHandler),
        (r"/messenger", SocketHandler)
    ], debug=debug, **settings)


if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    port_num = 5000
    port = int(os.environ.get("PORT", port_num))
    http_server.listen(port)
    print("Running my website at 127.0.0.1:" + str(port_num) + "...")
    tornado.ioloop.IOLoop.current().start()



