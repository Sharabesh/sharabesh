import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/index.html")
class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/contact.html")




settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")

}


def make_app():
    return tornado.web.Application([
        (r"/static/(.*)",tornado.web.StaticFileHandler,
         dict(path=settings["static_path"])),
        (r"/", MainHandler),
        (r"/contact",ContactHandler)
    ], debug=True)



if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    print("Running my website at 127.0.0.1:5000...")
    tornado.ioloop.IOLoop.current().start()
