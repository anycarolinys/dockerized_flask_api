from flask import Flask
from dotenv import load_dotenv
import os
from .extensions import database
from .routes import blueprint

def create_app():
    load_dotenv()

    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(app)

    # Registrar rotas
    with app.app_context():
        app.register_blueprint(blueprint)
        database.create_all()

    return app
