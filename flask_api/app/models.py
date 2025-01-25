# from . import database
from app.extensions import database

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(255), nullable=False)
    # birth_date = database.Column(database.Column(database.Date), nullable=False)
    birth_date = database.Column(database.Date, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_date": self.birth_date
        }
