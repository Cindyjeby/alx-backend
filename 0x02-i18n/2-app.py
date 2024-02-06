#!/usr/bin/env python3
"""A basic fask app"""

from flask_babel import Babel
from flask import Flask, render_template

class Config:
    """reps the flask babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """retrives the locale of a webpage"""
    return request.accept_language.best_match(app.config["LANGUAGES"])

@app.route('/')
def get_index() -> str:
    """index page"""
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
