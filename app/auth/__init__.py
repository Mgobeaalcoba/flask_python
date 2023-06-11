from flask import Blueprint

# Creo el blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')
# El prefijo significa que todas las rutas que comiencen con /auth van a redirigir a este blueprint

# Creo las vistas de este blueprint en un archivo que se llame views.py dentro del modulo y las importo acá:
from . import views
