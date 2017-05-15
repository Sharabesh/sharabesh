import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
#Used to send emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    password = os.environ["PASSWORD"]
except:
    print("Mail Server Offline. Please load password to continue")



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/index.html",failure=0)
class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/contact.html")
    def post(self):
        name=self.get_body_argument("name")
        fromaddr = self.get_body_argument("email")
        phone_number= self.get_body_argument("phone")
        message= self.get_body_argument("message")
        toaddr="sharabesh@berkeley.edu"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Contact from my website"

        body = "Name: {0}".format(name)
        body += "\n"
        body += "Phone Number: {0}".format(phone_number)
        body += "\n"
        body += "From: {0}".format(fromaddr)
        body += "\n"
        body += message

        msg.attach(MIMEText(body,'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("sharabesh97@gmail.com", password)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            self.redirect("/")
        except:
            self.render("static/html/index.html",failure=1)


class EducationHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/education.html")

class KernalHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/Kernels.html")


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")

}


def make_app():
    return tornado.web.Application([
        (r"/static/(.*)",tornado.web.StaticFileHandler,
         dict(path=settings["static_path"])),
        (r"/", MainHandler),
        (r"/contact",ContactHandler),
        (r"/education",EducationHandler),
        (r"/coding",KernalHandler)
    ], debug=True, compress_response=True)



if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    print("Running my website at 127.0.0.1:5000...")
    tornado.ioloop.IOLoop.current().start()
