#!/usr/bin/env python3
"""
This script setups a basic Flask app. Serves a single route,
that renders a welcome page.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def get_index() -> str:
    """
    Render the index page witha welcome message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
