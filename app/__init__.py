from flask import Flask
from dotenv import load_dotenv
import os
from .extensions import database
from .routes import blueprint

def create_app():
    """
    Cria e configura uma aplicação Flask.

    Carrega variáveis de ambiente usando dotenv, configura o banco de dados,
    inicializa extensões e registra rotas.

    Retorna:
        app (Flask): Instância configurada da aplicação Flask.
    """
    
    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()

    # Criar a aplicação Flask
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(app)

    # Registrar rotas
    with app.app_context():
        # Registrar blueprint para rotas
        app.register_blueprint(blueprint)
        # Criar todas as tabelas no banco de dados
        database.create_all()

    return app
