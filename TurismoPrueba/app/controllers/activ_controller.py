from flask import render_template, request, redirect, url_for
from app.models.db import db
from app.models.Actividad import Actividad

def listar_actividades():
    actividad = Actividad.query.all()
    return render_template('tempactiv/listar_actividades.html', actividad=actividad)

def create_actividad():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        destino_id = request.form['destino_id']
        nuevo_actividad = Actividad(nombre=nombre, descripcion=descripcion, destino_id=destino_id,precio=precio)
        db.session.add(nuevo_actividad)
        db.session.commit()
        return redirect(url_for('routes.listar_actividades'))
    return render_template('tempactiv/editar_actividad.html')

def edit_actividad(actividad_id):
    actividad = Actividad.query.get(actividad_id)
    if request.method == 'POST':
        actividad.nombre = request.form['nombre']
        actividad.descripcion = request.form['descripcion']
        actividad.precio = request.form['precio']
        db.session.commit()
        return redirect(url_for('routes.listar_actividades'))
    return render_template('tempactiv/editar_actividad.html', actividad=actividad)

def delete_actividad(actividad_id):
    actividad = Actividad.query.get(actividad_id)
    db.session.delete(actividad)
    db.session.commit()
    return redirect(url_for('routes.listar_actividades'))