#!/usr/bin/env python3
"""
This script is a Flask app with i18n that supports using flask-babel
and parameterized translations
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """
    Configuration class for Babel.

    Defines the supported languages and default locale & timezone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Select the best matching language
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Render the index page with localized messages.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
