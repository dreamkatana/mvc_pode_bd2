from db import db


# Define the SQLAlchemy model for the search history
class ModeloBusca(db.Model):
    __tablename__ = "buscas"

    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15), nullable=False)
    pokemon_name = db.Column(db.String(50), nullable=False)