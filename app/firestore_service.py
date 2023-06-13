import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Defino mi project_id para poder encender el server:
project_id = 'mgobea-flask'

# Hacemos una credencial default quees por ello que antes hicimos un login default:
credential = credentials.ApplicationDefault()
# Inicializo firebase con mis credenciales: 
firebase_admin.initialize_app(credential, {
    'projectId': project_id
})

# Creo una nueva instancia de un servicio o cliente de Firestore:
db = firestore.client()

# Pruebo que mi conexión esté resultando con una función para obtener todos mis usuarios: 
# @login_manager.user_loader # Decorador que traigo de mi objeto login_manager para evitar error "Missing user_loader or request_loader"
def get_users(): 
    return db.collection('users').get()

# Metodo que nos regresará un usuario especifico: 
def get_user(user_id):
    return db.collection('users').document(user_id).get()

# Armo mi segunda función para esta vez traer mis todos de mi database Firebase: 
def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()

# Armo una función para insertar en mi database un nuevo usuario: 
def post_user(user_data):
    # Creo mi nuevo documento donde el id es el username
    user_ref = db.collection('users').document(user_data.username)
    # Defino el password de este nuevo usuario que es el unico campo de mi document:
    user_ref.set({
        'password': user_data.password
    })
