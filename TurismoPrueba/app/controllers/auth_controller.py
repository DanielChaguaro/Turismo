from flask import render_template, request, redirect, url_for, session, flash
from app.models.Usuario import Usuario

def login():
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']
        user = Usuario.query.filter_by(email=email).first()
        if user and user.contrasena==contrasena:
            session['user_id'] = user.id
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Credenciales incorrectas.')
    return render_template('login.html')
    