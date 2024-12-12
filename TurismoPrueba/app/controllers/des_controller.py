from flask import render_template, request, redirect, url_for
from app.models.db import db
from app.models.Destino import Destino

def listar_destinos():
    destino = Destino.query.all()
    return render_template('tempdest/listar_destinos.html', destino=destino)

def create_destino():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        region = request.form['region']
        temporada_recomendada = request.form['temporada_recomendada']
        nuevo_destino = Destino(nombre=nombre, descripcion=descripcion, region=region,temporada_recomendada=temporada_recomendada)
        db.session.add(nuevo_destino)
        db.session.commit()
        return redirect(url_for('routes.listar_destinos'))
    return render_template('tempdest/editar_destino.html')

def edit_destino(destino_id):
    destino = Destino.query.get(destino_id)
    if request.method == 'POST':
        destino.nombre = request.form['nombre']
        destino.descripcion = request.form['descripcion']
        destino.region = request.form['region']
        destino.temporada_recomendada = request.form['temporada_recomendada']
        db.session.commit()
        return redirect(url_for('routes.listar_destinos'))
    return render_template('tempdest/editar_destino.html', destino=destino)

def delete_destino(destino_id):
    destino = Destino.query.get(destino_id)
    db.session.delete(destino)
    db.session.commit()
    return redirect(url_for('routes.listar_destinos'))
