from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
login =LoginManager(app)
login.login_view = 'login'
# login.login_message = "User needs to be logged in to view this page"


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models