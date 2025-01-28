# from . import database
from app.extensions import database

class User(database.Model):
    """
    Modelo que representa um usuário no banco de dados.

    Atributos:
        id (int): Identificador único do usuário (chave primária).
        name (str): Nome do usuário (obrigatório).
        birth_date (date): Data de nascimento do usuário (obrigatório).
    """
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(255), nullable=False)
    # birth_date = database.Column(database.Column(database.Date), nullable=False)
    birth_date = database.Column(database.Date, nullable=False)

    def to_dict(self):
        """
        Converte os dados do usuário para um dicionário.

        Retorna:
            dict: Dados do usuário em formato de dicionário.
        """
        return {
            "id": self.id,
            "name": self.name,
            "birth_date": self.birth_date
        }
