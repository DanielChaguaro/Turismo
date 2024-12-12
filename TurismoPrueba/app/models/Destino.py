from app.models.db import db

class Destino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    region = db.Column(db.String(100))
    temporada_recomendada = db.Column(db.String(100))