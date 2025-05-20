#!/usr/bin/env python3
"""
A Flask app with i18n support and url-based locale override.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """
    Configuration for the Flask app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match locale from the request query.
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Render the index page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
