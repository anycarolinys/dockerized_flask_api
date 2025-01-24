# https://flask.palletsprojects.com/en/stable/patterns/sqlalchemy/

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from .routes import blueprint

database = SQLAlchemy()

def api():
    load_dotenv()

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['ALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(api)

    with app.app_context():
        app.register_blueprint(blueprint)
        database.create_all()


    return app
