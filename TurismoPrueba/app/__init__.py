from flask import Flask
from app.models.db import configure_db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'tu_clave_secreta'  # Cambia esto por una clave segura

    # Configura la base de datos
    configure_db(app)

    # Registra las rutas
    from app.routes import routes
    app.register_blueprint(routes)

    return app