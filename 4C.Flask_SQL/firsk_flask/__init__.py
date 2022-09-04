from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db= SQLAlchemy()

def create_app():
    app=Flask(__name__)

    from firsk_flask.usersql.views import mod as users_module
    db.init_app(app)

    app.register_blueprint(usrs_module)
    return App

