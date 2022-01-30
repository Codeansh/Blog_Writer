from flask import Flask

app_ = Flask(__name__)

from app import routes
