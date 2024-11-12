import os
from dotenv import load_dotenv
import smtplib, ssl

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "strickland.wang@gmail.com"
    password = os.getenv('EMAIL_PASSWORD')

    receiver = "strickland.wang@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
