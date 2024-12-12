from app.models.db import db

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', back_populates='reservas', overlaps="reservas_usuario,usuarioreserva")
    actividad_id = db.Column(db.Integer, db.ForeignKey('actividad.id'), nullable=False)
    actividad = db.relationship('Actividad', backref=db.backref('reservas', lazy=True))
    fecha = db.Column(db.DateTime, nullable=False)