import bson
import os
import json
import math
import requests
import base64

from flask import url_for, request, session, redirect, make_response
from flask import Flask, render_template, abort, g
from flask_babel import gettext
from flask_app import flask_app, babel

import settings
import basic
import sendmail

# ------------------------------------------------------------------------
@flask_app.route("/contact/", methods=["POST"])
def contact():
    try:
        name = request.form["name"]
        email = request.form["email_address"]
        message = request.form["message"]

        sendmail.send(settings.NO_REPLY_EMAIL, settings.CONTACT_EMAIL,
                   gettext("Message from contact form; user '%(name)s', e-mail '%(email)s'",
                           name=name, email=email), message)
    except Exception as e:
        return make_response(gettext("Error"), 400)

    return make_response(gettext("The message is sent"), 200)

# ------------------------------------------------------------------------
# to avoid the locale parameter in every request handler
@flask_app.before_request
def before():
    if request.view_args and 'locale' in request.view_args:
        session["locale"] = request.view_args['locale']
        request.view_args.pop('locale')

# ------------------------------------------------------------------------
@babel.localeselector
def get_locale():
    # return "en"
    # uncomment to actually handle locale

    locale = session.get('locale', None)

    if locale is not None:
        return locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits. The best match wins.
    return request.accept_languages.best_match(['en', 'ru'])

# ------------------------------------------------------------------------
@flask_app.route('/')
def root():
    # locale = getattr(g, 'locale', None)
    locale = get_locale()

    guessed_locale = request.accept_languages.best_match(['en', 'ru'])
    if not guessed_locale:
        guessed_locale = flask_app.config['BABEL_DEFAULT_LOCALE']

    return redirect(url_for('index',
                            locale=locale if locale is not None else guessed_locale))

# ------------------------------------------------------------------------
@flask_app.route("/<locale>")
def index():
    switch_locales = dict(en="ru", ru="en")
    cur_locale = str(get_locale())
    return render_template("home.html",
                           is_logged_in=basic.is_logged_in(session),
                           switch_locale=switch_locales[cur_locale],
                           locale=cur_locale.capitalize())

# ------------------------------------------------------------------------
@flask_app.route("/fetch/")
def fetch():
    url = request.args['url']
    r = requests.get(url)
    data = base64.b64encode(r.content)
    mime_type = r.headers['Content-Type']
    resp = make_response('data:{};base64,{}'.format(mime_type, data.decode('utf-8')))
    resp.headers['Content-Type'] = mime_type
    return resp

