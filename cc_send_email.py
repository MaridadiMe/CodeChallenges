"""
This module provides a function to send an email
My implementation used mailtrap as smtp server
"""


import smtplib
from socket import gaierror

HOST = 'smtp.mailtrap.io'
SENDER = 'youremail@email.someting'
PORT = 465
USERNAME = '2ba887xxxxxxxxxx49b'
PASSWORD = '6417xxxxxxxxxxxxc6ccb018'
RECEIVER = 'receiveremail@gmail.com'

message = f"""\
Subject: Hi Mailtrap
To: {RECEIVER}
From: {SENDER}

This is my first message with Python.
"""

def send_email(receiver, sender, message):
    try:
        with smtplib.SMTP(HOST, PORT) as server:
            server.login(USERNAME, PASSWORD)
            server.sendmail(sender, receiver, message)
    except (gaierror, ConnectionRefusedError):
        print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))


if __name__ == "__main__":
    # test sending that email
    send_email(RECEIVER, SENDER, message)
