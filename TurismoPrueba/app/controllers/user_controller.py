from flask import render_template, request, redirect, url_for
from app.models.db import db
from app.models.Usuario import Usuario

def dashboard():
    users = Usuario.query.all()
    return render_template('tempuser/dashboard.html', users=users)

def create_user():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        contrasena = request.form['contrasena']
        preferencias= request.form['preferencias']
        nuevo_usuario = Usuario(nombre=nombre, email=email, contrasena=contrasena,preferencias=preferencias)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('routes.dashboard'))
    return render_template('tempuser/user_form.html')

def edit_user(user_id):
    user = Usuario.query.get(user_id)
    if request.method == 'POST':
        user.nombre = request.form['nombre']
        user.email = request.form['email']
        user.preferencias= request.form['preferencias']
        db.session.commit()
        return redirect(url_for('routes.dashboard'))
    return render_template('tempuser/user_form.html', user=user)

def delete_user(user_id):
    user = Usuario.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('routes.dashboard'))
