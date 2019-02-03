import tornado.websocket
import tornado.web
import json

# TODO: Very hacky but this is for a one-off just testing thing
CONN = None


class RemainderHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/html/remainder.html")


class SocketHandler(tornado.web.RequestHandler):
    def post(self):
        command = self.get_argument("command")
        print(command)
        try:
            CONN.write_message(command)
            self.write(json.dumps({
                "success": 1,
                "message": "It probably worked?"
            }))
        except Exception as e:
            print(e)
            self.write(json.dumps({
                "success": 0,
                "message": "Didn't work :("
            }))


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        global CONN
        CONN = self
        print("Opened Socket")

    def on_message(self,message):
        pass


    def on_close(self):
        print("Closed Socket")