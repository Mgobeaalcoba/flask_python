import unittest

from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app
from app.firestore_service import get_users, get_todos, post_todo, delete_todo
from app.forms import TodoForm, DeleteTodoForm 

# Inicializo una instancia de Flask
app = create_app() # Le paso como nombre el nombre de este archivo.

# Creo mi comando para ejecutar las pruebas automatizadas al correr "flask test" en terminal:
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

# todos = ["Comprar Cafe", "Llevar a los chicos al cole", "Estudiar en Platzi", "Entregar proyecto en Mercado Libre"] # Paso "todos" también al template

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
@login_required
def hello():
    # user_ip = request.cookies.get("user_ip") # Tomo el dato de IP ya no desde remote_addr sino desde la cookie que guarde en la def de arriba
    user_ip = session.get("user_ip")
    # login_form = LoginForm()
    # username = session.get('username') # Obtengo mi username de mi session. Luego de haberlo enviado vía post
    username = current_user.id

    # todos = []

    # for todo in get_todos(username):
    #     todos.append(todo.to_dict()['description'])

    # Instanceo un TodoForm: 
    todo_form = TodoForm()

    # Instanceo un DeleteTodoForm
    delete_todo_form = DeleteTodoForm()

    context = {
        'user_ip': user_ip,
        'username': username,
        'todos': get_todos(username), # Importante no olvidar la ultima coma en el dict para que expanda todas las variables.
        'todo_form': todo_form,
        'delete_todo_form': delete_todo_form,
    }

    if todo_form.validate_on_submit():
        todo = todo_form.description.data
        post_todo(username, todo)

        return redirect(url_for('index'))

    # La acción sobre el botón de completar se realiza sobre el HTML mismo

    # # Si mi route acepta request post entonces puedo usar esos datos.
    # if login_form.validate_on_submit():
    #     username = login_form.username.data # Todo el username del post para guardarlo en la sesion
    #     session['username'] = username # Guardo el username en mi sessión para luego usarlo en el "GET"

    #     # Guardo un flash en memoría que luego debo reenderiarlo en HTML:
    #     flash('Nombre de usuario registrado con exito!')

    #     # Redirijo a index en caso de que completen el form:
    #     return redirect(url_for('index'))

    # users = get_users() # Nos devuelve una lista de usuarios sobre la cual vamos a poder iterar

    # for user in users:
    #     print(user.id)
    #     print(user.to_dict()['password']) # El print en este caso será por consola. No en el template.

    
    # # Este return es para si nos hacen un "GET":
    return render_template('hello.html', **context) # Hello World Flask. tu IP es 127.0.0.1.
    # # Los ** son para expandir el diccionario y transformarlo en variables sueltas. 

@app.route("/test_server_error")
def test_server_error():
    raise(Exception('500 error'))

@app.route("/todos/delete/<todo_id>", methods=['GET', 'POST']) # Dinamic route en flask usa "< >" en lugar de "{}" como se usa en Fast Api
def delete(todo_id): # El todo_id viene desde la ruta en este caso. No desde un form
    user_id = current_user.id
    delete_todo(user_id, todo_id)
    
    return redirect(url_for('index'))
