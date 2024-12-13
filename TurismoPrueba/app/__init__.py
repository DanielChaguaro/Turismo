from flask import Flask
from app.models.db import configure_db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'hola' 

    configure_db(app)

    from app.routes import routes
    app.register_blueprint(routes)

    return app