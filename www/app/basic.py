import settings

import os

# from flask import render_template
# from smtplib import SMTP, SMTP_SSL
# from email.mime.text import MIMEText


def is_get(method):
    return method == "GET"

def is_post(method):
    return method == "POST"

def allowed_file(filename):
    base, ext = os.path.splitext(filename)
    return ext in settings.ALLOWED_EXTENSIONS


def is_logged_in(session):
    return "user" in session

# # ------------------------------------------------------------------------
# def send_email(to_address, from_address,
#                subject, message,
#                username, password,
#                smtp_server=settings.SMTP_SERVER,
#                smtp_port=settings.SMTP_PORT,
#                mail_type="html"):
#     message = MIMEText(message, mail_type)
#
#     message['Subject'] = subject
#     message['From'] = from_address
#     message['To'] = to_address
#
#     with SMTP_SSL(smtp_server, smtp_port) as s:
#         s.login(username, password)
#         s.send_message(message)
#
# # ------------------------------------------------------------------------
# def send_email_template(to_address, from_address,
#                         subject, template,
#                         username, password,
#                         smtp_server=settings.SMTP_SERVER,
#                         smtp_port=settings.SMTP_PORT,
#                         **template_kwargs):
#     send_email(to_address,
#                from_address,
#                subject,
#                render_template(template, **template_kwargs),
#                username,
#                password,
#                smtp_server,
#                smtp_port)