#!/usr/bin/env python3
"""
This is a Flask app with i18n with support for using Flask-Babel
and dynamic locale selection.
"""

from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    """
    Selects the best matching language

    Returns:
        The best match language code as a string.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Render the index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
