from app.models.db import db

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('comentarios', lazy=True))
    actividad_id = db.Column(db.Integer, db.ForeignKey('actividad.id'), nullable=False)
    actividad = db.relationship('Actividad', backref=db.backref('comentarios', lazy=True))
    texto = db.Column(db.Text, nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)