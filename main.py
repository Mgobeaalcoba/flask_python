from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm 
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest


# Inicializo una instancia de Flask
app = Flask(__name__) # Le paso como nombre el nombre de este archivo.

# Inicializo una instancia de Bootstrap
bootstrap = Bootstrap5(app)

# Armo mí secret key para ocultar los datos sensibles del usuario: 
app.config["SECRET_KEY"] = 'SUPER SECRETO' # Al pasar a production luego vamos a encriptar este dato que es lo correcto. 

# Class LoginForm que hereda de FlaskForm:
class LoginForm(FlaskForm):
    # Los forms tienen campos o field que deben llenarse:
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) # WTF va a manejar pertinentemente estos password. Es decir de forma segura.
    # Agregamos un validador de datos que también lo tiene WTF
    # Agregamos un SubmitField como botón de envio:
    submit = SubmitField("Enviar")

# Creo mi comando para ejecutar las pruebas automatizadas al correr "flask test" en terminal:
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

todos = ["Comprar Cafe", "Llevar a los chicos al cole", "Estudiar en Platzi", "Entregar proyecto en Mercado Libre"] # Paso "todos" también al template

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello")) # Redirección guardada en variable
    # response.set_cookie("user_ip", user_ip) # Guardo IP en Cookie.
    session['user_ip'] = user_ip

    return response # Retornamos una respuesta de flask que en este caso es un redirect

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    # user_ip = request.cookies.get("user_ip") # Tomo el dato de IP ya no desde remote_addr sino desde la cookie que guarde en la def de arriba
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    username = session.get('username') # Obtengo mi username de mi session. Luego de haberlo enviado vía post

    context = {
        'user_ip': user_ip,
        'username': username,
        'todos': todos, # Importante no olvidar la ultima coma en el dict para que expanda todas las variables.
        'login_form': login_form,
    }

    # Si mi route acepta request post entonces puedo usar esos datos.
    if login_form.validate_on_submit():
        username = login_form.username.data # Todo el username del post para guardarlo en la sesion
        session['username'] = username # Guardo el username en mi sessión para luego usarlo en el "GET"

        # Guardo un flash en memoría que luego debo reenderiarlo en HTML:
        flash('Nombre de usuario registrado con exito!')

        # Redirijo a index en caso de que completen el form:
        return redirect(url_for('index'))
    
    # Este return es para si nos hacen un "GET":
    return render_template('hello.html', **context) # Hello World Flask. tu IP es 127.0.0.1.
    # Los ** son para expandir el diccionario y transformarlo en variables sueltas. 

@app.route("/test_server_error")
def test_server_error():
    raise(Exception('500 error'))

