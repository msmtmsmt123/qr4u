import settings

from flask import Flask
from flask_babel import Babel
from babel.support import Translations

flask_app = Flask(__name__)
flask_app.secret_key = "\x81\xb6\xee\xbdep\xff\\\xfbu\xec~R\xb8S\x12\xddm0\x0e\xdc\xdc\x07\xee"
babel = Babel(flask_app)

Translations.DEFAULT_DOMAIN = "strings"
flask_app.config['BABEL_DEFAULT_LOCALE'] = settings.DEFAULT_LOCALE

