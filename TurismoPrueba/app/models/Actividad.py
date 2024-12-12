from app.models.db import db

class Actividad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    destino_id = db.Column(db.Integer, db.ForeignKey('destino.id'), nullable=False)
    destino = db.relationship('Destino', backref=db.backref('actividades', lazy=True))
    precio = db.Column(db.Float, nullable=False)