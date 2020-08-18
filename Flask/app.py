"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask

APP = Flask(__name__)


@APP.route('/')
def root():
    """Base view."""
    return 'Hello!'
