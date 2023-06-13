# Importaciones de Flask y sus librerías: 
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

# Importo mi Config para luego configurar con ella mi app: 
from .config import Config
# Importo mi blueprint para poder registrarlo luego en app:
from .auth import auth
# Importo mi UserModel
from .models import UserModel

# Instanceo un obejto LoginManager
login_manager = LoginManager()
# Le explicito a mi objeto sobre que route va a a trabajar: 
login_manager.login_view = 'auth.login'

# Implementamos la función load_user que va a implementar el metodo estatico query
# para traerse desde la base de datos a nuestro User: 
@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)

    # Configuro mi aplicación desde un objeto Config.
    app.config.from_object(Config)

    # Le indico a mi objeto login_manager que inicialice la app: 
    login_manager.init_app(app)

    # Registro el blueprint creado para "auth" dentro de mi app. Sino fallará el test donde veo que exista. 
    app.register_blueprint(auth)

    return app