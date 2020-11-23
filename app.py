import requests
from flask import Flask, render_template
from script import scrapper
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return scrapper()
