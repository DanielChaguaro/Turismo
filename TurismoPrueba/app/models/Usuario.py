from app.models.db import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(200), nullable=False)
    preferencias = db.Column(db.String(200)) 
    
    #reservas_usuario = db.relationship('Reserva', backref=db.backref('usuarioreserva', lazy=True))
    reservas = db.relationship('Reserva', back_populates='usuario', lazy=True, overlaps="reservas_usuario,usuarioreserva")
    # Propiedad para acceder al historial de actividades
    @property
    def historial(self):
        return [reserva.actividad_id for reserva in self.reservas]