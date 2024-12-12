from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:12345678@DESKTOP-T5KGBI3\SQLEXPRESS/TurismoPrueba?driver=ODBC+Driver+17+for+SQL+Server'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)