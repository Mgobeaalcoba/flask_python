from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap5

# Inicializo una instancia de Flask
app = Flask(__name__) # Le paso como nombre el nombre de este archivo.

# Inicializo una instancia de Bootstrap
bootstrap = Bootstrap5(app)

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
    response.set_cookie("user_ip", user_ip) # Guardo IP en Cookie.

    return response # Retornamos una respuesta de flask que en este caso es un redirect

@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip") # Tomo el dato de IP ya no desde remote_addr sino desde la cookie que guarde en la def de arriba
    context = {
        'user_ip': user_ip,
        'todos': todos, # Importante no olvidar la ultima coma en el dict para que expanda todas las variables.
    }
    return render_template('hello.html', **context) # Hello World Flask. tu IP es 127.0.0.1.
    # Los ** son para expandir el diccionario y transformarlo en variables sueltas. 

@app.route("/test_server_error")
def test_server_error():
    raise(Exception('500 error'))

