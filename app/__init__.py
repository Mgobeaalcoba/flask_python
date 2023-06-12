from flask import Flask
from flask_bootstrap import Bootstrap5

# Importo mi Config para luego configurar con ella mi app: 
from .config import Config
# Importo mi blueprint para poder registrarlo luego en app:
from .auth import auth

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)

    # Configuro mi aplicación desde un objeto Config.
    app.config.from_object(Config)

    # Registro el blueprint creado para "auth" dentro de mi app. Sino fallará el test donde veo que exista. 
    app.register_blueprint(auth)


    return app