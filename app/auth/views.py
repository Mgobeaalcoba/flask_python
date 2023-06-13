from flask import render_template, session, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user

from app.forms import LoginForm
from app.firestore_service import get_user
from app.models import UserData, UserModel
from . import auth



@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    # Si mi route acepta request post entonces puedo usar esos datos.
    if login_form.validate_on_submit():
        # Validamos si el usuario se encuentra en nuestra base de datos o no: 
        ## Obtenemos el username que nos envío y su password
        username = login_form.username.data # Tomo el username del post para guardarlo en la sesion
        password = login_form.password.data # Tomo el password del post hecho mediante form

        ## Traigo el documento de firestore que coincide con el usuario que se registró
        user_doc = get_user(username) # Si no existe el user nos va a devolver un document snapshot con información vacia

        if user_doc.to_dict() is not None: # Valido si hay información en lo que me devolvió firebase
            password_from_db = user_doc.to_dict()['password']

            ### Valido que el password del form sea el mismo que el password de la database: 
            if password == password_from_db:
                ### Armo user_data y user_model para enviarlo a flask-login:
                user_data = UserData(
                    username= username,
                    password= password
                )
                user = UserModel(
                    user_data
                )
                # Uso la función de login_user de flask-login para loguear mi user:
                login_user(user) # Login completado
                # Flasheamos un mensaje de bienvenida para el usuario logueado: 
                flash('Bienvenido de nuevo')
                # Debemos redirigir ahora hacia el index de mi web app ("/")
                redirect(url_for('index'))
            else:
                flash('La información no coincide con nuestra base de datos')
        else:
            flash('El usuario ingresado no existe')
            
        # session['username'] = username # Guardo el username en mi sessión para luego usarlo en el "GET"

        # Guardo un flash en memoría que luego debo reenderiarlo en HTML:
        # flash('Nombre de usuario registrado con exito!')

        # Redirijo a index en caso de que completen el form:
        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')
    
    return redirect(url_for('auth.login'))
