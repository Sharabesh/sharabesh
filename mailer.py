from tornado.httpclient import  AsyncHTTPClient
from urllib.parse import urlencode
from tornado.httpclient import HTTPRequest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import json

server = None  # Initializing global email server object to prevent regional login requests
DESTINATION_EMAIL = os.environ["TOSITE"]
SOURCE_EMAIL = os.environ["FROMSITE"]
CAPTCHA_SECRET = os.environ["CAPTCHA_SECRET"]


try:
    password = os.environ["PASSWORD"]
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(SOURCE_EMAIL, password)
    print("Successful Login")
except:
    print("Mail Server Non-Functional at the moment. Unable to log in.")
    server = None



async def validate_captcha(recieved_captcha):
    try:
        http_client = AsyncHTTPClient()
        data = {
            'secret': CAPTCHA_SECRET,
            'response': recieved_captcha
        }
        request = HTTPRequest("https://www.google.com/recaptcha/api/siteverify", "POST", body=urlencode(data))
        x = await http_client.fetch(request)
        captcha_status = json.loads(x.body)

        if captcha_status['success'] != True:
            return False
        return True
    except:
        return False



def compose_email(name, from_addr, message, phone_number):
    toaddr = DESTINATION_EMAIL
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = toaddr
    msg['Subject'] = "Contact from my website"

    body = f"""
    Name: {name} 
    Phone Number: {phone_number}
    From: {from_addr} 
    
    
    Message: 
    {message} 
    """

    msg.attach(MIMEText(body, 'plain'))
    return msg


async def issue_message(name, from_addr, phone_number, message, captcha):
    global server
    captcha_validation = await validate_captcha(captcha)
    if not captcha_validation:
        return False, "This message has been flagged as coming from a bot account please try through other means!"
    else:
        try:
            message = compose_email(name, from_addr, message, phone_number)
            if not server:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(SOURCE_EMAIL, password)
            text = message.as_string()
            server.sendmail(from_addr, DESTINATION_EMAIL, text)
            return True, "Success!\nYou should receive a response shortly"
        except:
            return False, "Unfortunately, the mail server is down. Please contact Sharabesh directly through sharabesh (at) berkeley.edu"




