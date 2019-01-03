import os
# Modules to run webserver
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
from models import *
# Used to send emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


DESTINATION_EMAIL = os.environ["TOSITE"]
SOURCE_EMAIL = os.environ["FROMSITE"]

server = None  # Initializing global email server object to prevent regional login requests
try:
    password = os.environ["PASSWORD"]
except KeyError:
    print("Mail Server Offline. Please load password to continue")


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
    def post(self):
        global server
        try:
            name = self.get_body_argument("name")
        except BaseException:
            self.redirect("/contact")
            return
        fromaddr = self.get_body_argument("email")
        phone_number = self.get_body_argument("phone")
        message = self.get_body_argument("message")
        toaddr = DESTINATION_EMAIL

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Contact from my website"

        body = "Name: {0}".format(name)
        body += "\n"
        body += "Phone Number: {0}".format(phone_number)
        body += "\n"
        body += "From: {0}".format(fromaddr)
        body += "\n\n\n"
        body += "Message: "
        body += "\n"
        body += message

        msg.attach(MIMEText(body, 'plain'))

        try:
            if not server:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(SOURCE_EMAIL, password)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            self.render(
                "static/html/contact.html",
                failure=0,
                message="Success!\nYou will recieve a response shortly")
        except BaseException:
            self.render("static/html/contact.html", failure=1, message="")


class EducationHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/education.html")


class KernalHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/Kernels.html")


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
        (r"/coding", KernalHandler),
        (r"/response", ResponseHandler),
        (r"/cookie", CookieHandler),
    ], debug=debug, **settings)


if __name__ == "__main__":
    # try:
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.ehlo()
    #     server.starttls()
    #     server.login(SOURCE_EMAIL, password)
    #     print("I was able to successfully login to email from the server!")
    # except BaseException:
    #     server = None
    #     print("I was unable to login to the server")
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    port_num = 5000
    port = int(os.environ.get("PORT", port_num))
    http_server.listen(port)
    print("Running my website at 127.0.0.1:" + str(port_num) + "...")
    tornado.ioloop.IOLoop.current().start()



