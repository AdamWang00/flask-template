from flask_mail import Message
from flask import current_app
from website import mail


def send_contact_email(name, email, message):
    msg = Message('TEMPLATE Contact Form', sender='noreply10665@gmail.com', recipients=current_app.config['MAIL_TO'].split()) # cc=[email],
    msg.body = f'''Name: {name}
Email: {email}
Message: {message}
'''
    mail.send(msg)