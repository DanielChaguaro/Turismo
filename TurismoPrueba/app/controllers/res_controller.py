from flask import render_template, request, redirect, url_for,session
from app.models.db import db
from app.models.Reserva import Reserva
from app.models.Actividad import Actividad

def listar_reservas():
    reserva = Reserva.query.all()
    return render_template('tempreserva/listar_reservas.html', reserva=reserva)

def create_reserva(actividad_id):
    usuario_id = session.get('user_id')
    if request.method == 'POST':
        fecha = request.form['fecha']
        nuevo_reserva = Reserva(usuario_id=usuario_id,actividad_id=actividad_id,fecha=fecha)
        db.session.add(nuevo_reserva)
        db.session.commit()
        return redirect(url_for('routes.recomendaciones_basicas'))
    return render_template('tempreserva/editar_reserva.html')

def edit_reserva(reserva_id):
    reserva = Reserva.query.get(reserva_id)
    if request.method == 'POST':
        reserva.fecha = request.form['fecha']
        db.session.commit()
        return redirect(url_for('routes.listar_reservas'))
    return render_template('tempreserva/editar_reserva.html', reserva=reserva)

def delete_reserva(reserva_id):
    user = Reserva.query.get(reserva_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('routes.listar_reservas'))
