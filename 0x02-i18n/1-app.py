#!/usr/bin/env python3
"""
This script does a Flask app configuration for i18n,
Flask-Babel with support for English and French.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for Babel.

    Defines the supported languages and default locale & timezone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app: Flask = Flask(__name__)
app.config.from_object(Config)


babel: Babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Render the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
