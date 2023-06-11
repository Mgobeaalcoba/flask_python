from flask import Flask
from flask_bootstrap import Bootstrap5

from .config import Config
from .auth import auth

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)

    app.config.from_object(Config)

    # Registro el blueprint creado para "auth" dentro de mi app. Sino fallará el test donde veo que exista. 
    app.register_blueprint(auth)

    return app