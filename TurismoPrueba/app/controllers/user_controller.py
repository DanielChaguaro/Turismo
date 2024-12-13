import re
from flask import render_template, request, redirect, url_for, flash
from app.models.db import db
from app.models.Usuario import Usuario

def dashboard():
    users = Usuario.query.all()
    return render_template('tempuser/dashboard.html', users=users)

def es_email_valido(email):
    patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron_email, email)

def es_nombre_valido(nombre):
    return not any(char.isdigit() for char in nombre)

def es_contrasena_valida(contrasena):
    return len(contrasena) >= 8

def es_email_unico(email):
    return Usuario.query.filter_by(email=email).first() is None

def create_user():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        contrasena = request.form['contrasena']
        preferencias= request.form['preferencias']
        errores = []

        if not es_email_valido(email):
            errores.append("El correo electrónico no es válido.")
        if not es_email_unico(email):
            errores.append("El correo electrónico ya está registrado.")
        if not es_nombre_valido(nombre):
            errores.append("El nombre no debe contener números.")
        if not es_contrasena_valida(contrasena):
            errores.append("La contraseña debe tener al menos 8 caracteres.")

        if errores:
            for error in errores:
                flash(error, 'error')
            return render_template('tempuser/user_form.html', nombre=nombre, email=email, preferencias=preferencias)
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
