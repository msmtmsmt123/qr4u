#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os.path
import sys
import re
import logging
import unicodedata
import traceback

import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import mongoengine

from flask import url_for, request, session, redirect
from flask import Flask, render_template
from tornado.options import define, options
from tornado.wsgi import WSGIContainer
from tornado.web import FallbackHandler

import settings
import req_handler
import sendmail

from flask_app import flask_app

APP_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(APP_DIR)

class Application(tornado.web.Application):
    def __init__(self, flask_app):
        wsgi_container = WSGIContainer(flask_app)

        handlers = [
            (r".*", FallbackHandler, dict(fallback=wsgi_container)),
        ]
        s = dict(
            template_path=os.path.join(APP_DIR, "templates"),
            static_path=os.path.join(APP_DIR, "static"),
            xsrf_cookies=False,
            cookie_secret="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            #login_url="/login",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **s)


def main():
    """App entry point"""

    define("address", default="127.0.0.1", help="Run on the given ip")
    define("port", default=8080, help="Run on the given port", type=int)

    tornado.options.parse_command_line()

    app = Application(flask_app)
    app.listen(options.port, options.address)

    print('Starting forever loop...')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exception(*sys.exc_info())
        print("An error encountered: " + str(e))

