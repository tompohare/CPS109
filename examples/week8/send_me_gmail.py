"""
Send email using your gmail account.

Prerequisite:
Create a .env file in same directory as the program. Add your gmail
16-digit app password, include the double quotes around your password:

GMAIL_PASSWORD="16-digit app-password"

Open a bash terminal in PythonAnywhere and install the following module:

pip3.10 install --user python-dotenv

See also: 
1. https://myaccount.google.com/apppasswords
2. https://support.google.com/mail/answer/185833?hl=en
2. https://help.pythonanywhere.com/pages/InstallingNewModules
"""

from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env file
MY_GMAIL_ADDRESS = os.getenv('MY_GMAIL_ADDRESS')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD') # 16-digit app-password
smtp_port = 465  # For SSL
smtp_server = 'smtp.gmail.com'
sender_email = MY_GMAIL_ADDRESS  # Enter your address
receiver_email = MY_GMAIL_ADDRESS # Enter receiver address

def send(subject, content):
    msg = EmailMessage()
    msg.set_content(content, 'html') # message body in HTML format
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, GMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == '__main__':        
    send('Hello World from Python Gmail!', '<h1>Hello World!</h1>')