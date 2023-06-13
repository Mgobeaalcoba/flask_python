# Flask: framework de Python para crear App´s web

## ¿Como funcionan las aplicaciones web? 

Cuando utilizas una aplicación web puedes interactuar con ella desde una computadora hasta un dispositivo móvil, pero esto no quiere decir que consume el procesamiento de tu dispositivo. Todo lo contrario, se hace en una red de servidores.

Estos servidores unen su poder de procesamiento con el fin transmitir solicitudes a todo el mundo, a su vez utilizar servidores especializados para almacenar los datos con los cuales se está trabajando, así como los datos de los demás usuarios. Como todo esto sucede sin demora alguna, parecerá que la aplicación se está ejecutando de forma nativa en tu dispositivo.

El servidor procesa la información obtenida por el navegador, luego se realizan los procedimientos necesarios de acuerdo a la lógica de negocio de la aplicación para regresar la información solicitada al cliente.

Ejemplo:

Cuando utilizamos Google Drive el cual es una aplicación web y abrimos un documento con Google Docs, el navegador se comunica con los servidores para ver y editar el documento.

A medida que vayas editando el documento, tu navegador trabajará de la mano con los servidores para asegurarse que todos los cambios se estén guardando.

Ventajas:

Muchas de las aplicaciones web que existen son gratuitas.
Puedes acceder a tu información en cualquier momento y lugar.
No dependes de un dispositivo en específico ya que la aplicación se encuentra almacenada en la web.

<img src="./images/apps_web.PNG">

## ¿Que es Flask? Microframework

Aca dejo mis apuntes de esta clase

Flask es un microframework hecho en Python el cual una de sus grandes ventajas es que es simple y facil de personalizar a medida que la aplicación crezca también las dependencias que se van a utilizar.

Algunas diferencias de con Django son:

- Utiliza un template llamado Jinja2 que esta inspirado en los Django Templates.
- Django es todo incluido mientras que Flask es lo más simple posible.
- Django tiene un módelo MVC mientras que Flask no tiene un módelo especifico es libre.
- Django tiene ORM mientras que Flask es más personalizable al trabajar con bases de datos.

--------------------------------------------

## Encendido de Flask

Ademas de la creación de un venv y la instalación de flask vía PIP en el mismo debemos crear unaa variable de entorno para que el comando **flask run** funcione. Eso lo hacemos con: 

En Linux/Mac:

```bash
export FLASK_APP=main.py
```

En Windows:

```bash
set FLASK_APP=main.py
```

------------------------------------------

## Modo debugger en Flask

**Flask** tiene un modo debugger que nos va a permitir salvar cambios y que los mismos impacten directamente en nuestra app sin necesidad de apagar y volver a prender el server. Es un similar al flag "--reload" de uvicorn que usamos cuando trabajamos con fastapi

Tenemos dos formas de hacerlo:

1- crear una variable de entorno: 

En Linux/Mac:

```bash
export FLASK_DEBUG=1
```

En Windows:

```bash
set FLASK_DEBUG=1
```

2- Otra opción para correr el servidor en modo debug es poner estas lineas al final del archivo main.py:

```python
if __name__ == '__main__':
    app.run(debug=True)
```
y correr main.py desde la terminal:

```bash
python main.py 
```

-----------------------------------------

## Request y Response:

Flask provee varios tipos de variables que no brindan el contexto de nuestra aplicación una de ellas es request.
Para ello primero debemos de import **request** de Flask.

```python
from flask import Flask, request
```

-----------------------------------------

## Ciclos de Request y Response:

Request-Response: es uno de los métodos básicos que usan las computadoras para comunicarse entre sí, en el que la primera computadora envía una solicitud de algunos datos y la segunda responde a la solicitud.

Por lo general, hay una serie de intercambios de este tipo hasta que se envía el mensaje completo.

Por ejemplo: navegar por una página web es un ejemplo de comunicación de request-response.

Request-response se puede ver como una llamada telefónica, en la que se llama a alguien y responde a la llamada; es decir hacemos una petición y recibimos una respuesta.

Vamos a crear una nueva ruta, guardar el IP del usuario en una Cookie y vamos a redirigir al usuario a la ruta de hello

-----------------------------------------

## Templates con Jinja 2:

¿Que son los templates? ¿Como renderizar archivos HTML en nuestra aplicación? 

Un templeate -> archivo de HTML -> renderiza informacion: Estatica o DInamica -> por variables -> luego nos muestra en el navegador

Para renderizar un template/plantilla creada con Jinja2 simplemente hay que hacer uso del método render_template.

A este método debemos pasarle el nombre de nuestra template y las variables necesarias para su renderizado como parámetros clave-valor.

Flask buscará las plantillas en el directorio templates de nuestro proyecto. En el sistema de ficheros, este directorio se debe encontrar en el mismo nivel en el que hayamos definido nuestra aplicación. En nuestro caso, la aplicación se encuentra en el fichero main.py.

Es hora de crear este directorio y añadir las páginas main.html, La estructura de nuestro proyecto quedaría del siguiente modo:

```bash
Flask-proyect
|_main.py
|_ /templeate
    |__ hello.html
```
Ejemplo archivo main.py

```py
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello_world'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello_world')
def hello_world():
    #creamos nueva variable de la ip que detectamos en el browser
    user_ip = request.cookies.get('user_ip')

    return render_template('hello_world.html', user_ip= user_ip)
# metodo es render_template con jinja2 y la variable es user_ip.
```

Con los templates podemos, por ejemplo, en lugar de regresar (return) un string del tipo "Hello World..." regresar un archivo .html

--------------------------------------------------

## Estructuras de control y for loops en los templates:

**Iteración**: es la repetición de un segmento de código dentro de un programa de computadora. Puede usarse tanto como un término genérico (como sinónimo de repetición), así como para describir una forma específica de repetición con un estado mutable.

Un ejemplo de iteración sería el siguiente:

```html
<!-- Ciclo for en template HTML -->
<ul>
    {% for todo in todos %}
        <li>{{todo}}</li> 
    {% endfor %}    
</ul>
```

Un ejemplo de condicional sería este:

```html
<!-- Condicionales en template HTML -->
{% if user_ip %}
    <h2>Hello World, tu Ip es {{user_ip}} </h2>
{% else %}
    <a href="{{ url_for('index') }}">Ir a inicio</a>
{% endif %} 
```

--------------------------------------------------------

## Herencia de templates y macros:

**Uso de plantillas**

Uso de plantillas(Block)
Ejemplo de archivo padre:

```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>
            {% block title %} Flask Platzi | {% endblock %}
        </title>
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
    </html>
```
Ejemplo de archivo hijo(file.html)

```html
    {% extends './base.html' %}
    {% block title %}
        {{super()}}
        Bienvenido
    {% endblock %}

    {% block content %}
        <p>Bloque de contenido del archivo hijo </p>
    {% endblock %}
```

**Uso de Macros (funciones en plantillas)**

Macro: son un conjunto de comandos que se invocan con una palabra clave, opcionalmente seguidas de parámetros que se utilizan como código literal. Los Macros son manejados por el compilador y no por el ejecutable compilado.

Los macros facilitan la actualización y mantenimiento de las aplicaciones debido a que su re-utilización minimiza la cantidad de código escrito necesario para escribir un programa.

En este ejemplo nuestra macro se vería de la siguiente manera:

```html
{% macro nav_link(endpoint, text) %}
    {% if request.endpoint.endswith(endpoint) %}
        <li class="active"><a href="{{ url_for(endpoint) }}">{{text}}a>li>
    {% else %}
        <li><a href="{{ url_for(endpoint) }}">{{text}}a>li>
    {% endif %}
{% endmacro %}
```

Un ejemplo de uso de macros en Flask:

```html
{% from "macros.html" import nav_link with context %}

<html lang="en">
    <head>
    {% block head %}
        <title>My applicationtitle>
    {% endblock %}
    head>
    <body>
        <ul class="nav-list">
            {{ nav_link('home', 'Home') }}
            {{ nav_link('about', 'About') }}
            {{ nav_link('contact', 'Get in touch') }}
        ul>
    {% block body %}
    {% endblock %}
    body>
html>
```
Como podemos observar en la primera línea estamos llamando a macros.html que contiene todos nuestros macros, pero queremos uno en específico así que escribimos import nav_link para traer el macro deseado y lo renderizamos de esta manera en nuestro menú {{ nav_link('home', 'Home') }}.

### Mas ejemplos de uso de macros

Para crear componentes(funciones y código) se define un tipo(macro), el nombre de la funcion y los pámetros.

Ejemplo de estructura:

```html
    {% macro NAME_FUNCTION(PARAM_1, PARAM_2) %}
        <p>Bloque de contenido<p>
    {% endmacro %}
```

Ejemplo de uso:

```html
    {% macro render_item(todo) %}
        <li>Descripción: {{todo}} </li>
    {% endmacro %}
```
Se define un archivo home.html

```html
    {% import 'render_item_list.html' as macros %}

    {% for description in arrDescriptions %}
        {{ macros.render_item(description) }}
    {% endfor %}
```

----------------------------------------------

## Uso de archivos estaticos: Imagenes

La forma de usar archivos estaticos es similar al manejo de templates HTML. Es decir usamos el helper URL_FOR de flask para importar el archivo que necesitamos. 

**Uso de url_for**

La funcion url_for se puede utilizar para consumir archivos estaticos y redirecionar a otras páginas dentro del proyecto.

**Uso archivos estativos**

Se llaman a traves de la funcion url_for, tiene 2 parámetros:

1.- path = 'static’
2.- filename = [Ruta del archivo]

Ejemplo:

```html
<link rel="stylesheet" href="{{ url_for(path = 'static', filename = 'css/main.css')}}">
<img src="{{url_for(path = 'static', filename = 'images/platzi.png')}}">
```

**Uso de redireccionamiento a paginas**

Se realiza el redirecciónamiento a traves de la funcion url_for, en el primer
atributo, se explifica el path del archivo(ruta), ejemplo:

```html
<li><a href="{{url_for(path = 'index')}}">Inicio</a></li>
```

--------------------------------------------------------

## Manejo de errores para cuando el cliente quiere ir a paths inexistentes

**Configurar paginas de error**

**Status Code HTTP:**

**100**: no son errores sino mensajes informativos. Como usuario nunca los verás, sino que entre bambalinas indica que la petición se ha recibido y se continúa el proceso.

**200**: estos códigos también indican que todo ha ido correctamente. La petición se ha recibido, se ha procesado y se ha devuelto satisfactoriamente. Por tanto, nunca los verás en tu navegador, pues significan que todo ha ido bien.

**300**: están relacionados con redirecciones. Los servidores usan estos códigos para indicar al navegador que la página o recurso que han pedido se ha movido de sitio. Como usuario, no verás estos códigos, aunque gracias a ellos una página te podría redirigir automáticamente a otra.

**400**: corresponden a errores del cliente y con frecuencia sí los verás. Es el caso del conocido **error 404**, que aparece cuando la página que has intentado buscar no existe. Es, por tanto, un error del cliente (la dirección web estaba mal).

**500**: mientras que los códigos de estado 400 implican errores por parte del cliente (es decir, de parte tuya, tu navegador o tu conexión), los errores 500 son errores desde la parte del servidor. Es posible que el servidor tenga algún problema temporal y no hay mucho que puedas hacer salvo probar de nuevo más tarde.

El error 404 es el que vamos a manejar ahora...

Flask maneja estos errores con un decorador llamado **"errorhandler(StatusCode)"**

```python
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)
```

```html
<!-- Herencia de templates -->
{% extends 'base.html' %}

{% block title %}
    {{ super() }}
    404
{% endblock title %}

{% block content %}
    <h1>Lo sentimos. No encontramos lo que buscabas</h1>
{% endblock %}
```

Reto: Manejar el error 500 o Internal Server Error con Flask: 

```python
@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)
```
```python
@app.route("/test_server_error")
def test_server_error():
    raise(Exception('500 error'))
```

```html
<!-- Herencia de templates -->
{% extends 'base.html' %}

{% block title %}
    {{ super() }}
    500: Internal Server Error
{% endblock title %}

{% block content %}
    <h1>Lo sentimos</h1>
    <p>Ocurrió un error, estamos trabajando en ello</p>
{% endblock %}
```

Para poder testear con la path operation de "/test_server_error" vamos a tener que apagar el servidor de flask y configurar el mode debugger en "0" nuevamente. Es decir, apagarlo de la siguiente forma: 

Linux o Mac:
```bash
export FLASK_DEBUG=0
```

Windows:
```bash
set FLASK_DEBUG=0
```

--------------------------------------

## Flask cuenta con una serie de extensiones que te permiten otras utilidades como mandar mails o dar formato agradable a nuestra paginas

Particularmente vamos a trabajar con **Flask-Bootstrap** que es justamente un framework para dar contexto mas agradable a nuestras Web App´s. 

https://pythonhosted.org/Flask-Bootstrap/

Recordemos que es un **framework**:

Un conjunto estandarizado de conceptos, prácticas y criterios para enfocar un tipo de problemática particular que sirve como referencia, para enfrentar y resolver nuevos problemas de índole similar.

```bash
pip install Bootstrap-Flask==2.0.2
```

Importo la clase Bootstrap

```py
from flask_bootstrap import Bootstrap5
```

Inicializo un objeto de type Bootstrap:

```py
# Inicializo una instancia de Bootstrap
bootstrap = Bootstrap5(app)
```

Modifico mi base.html dado que Bootstrap ya tiene un base.html propio que vamos a extender: 

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        {% block head %}
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>
                {% block title %}
                    Flask Example - 
                {% endblock %}
            </title>

            {% block styles %}
                {{ bootstrap.load_css() }}
                <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}" />
            {% endblock %}
        {% endblock %}
    </head>
    <body>
        {% block body %}
            {% block navbar %}
                {% include "navbar.html" %}
            {% endblock %}
            {% block content %}
            {% endblock %}

            {% block scripts %}
                {{ bootstrap.load_js() }}
            {% endblock %}
        {% endblock %}
    </body>
</html>
```

Y finalmente altero mi navbar.html así:

```html
{% block navbar %}
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Flask Example</a>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('hello') }}">
                            Inicio
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://github.com/Mgobeaalcoba" target="_blank">
                            @Mgobeaalcoba
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
{% endblock %}
```

---------------------------------------------

## Configuración de Flask

Por default Flask trabaja en **production mode** pero no deberíamos trabajar de este modo cuando estamos armando nuestra web app sino que deberiamos hacerlo en **development mode**. Para que esto ocurra debemos hacerlo de la siguiente forma: 

en Linux/Mac:

```bash
export FLASK_ENV=development
echo $FLASK_ENV
```

en Windows:

```bash
set FLASK_ENV=development
```

Al reencender el servidor con flask run vamos a encontrarnos entonces con que se enciende en "development server"

```bash
flask run
```

Para proteger los datos del usuario que guardamos en cookies necesitamos encriptar esta información. Y esto con Flask lo podemos hacer mediante el uso de **SESSION**

SESSION: es un intercambio de información interactiva semipermanente, también conocido como diálogo, una conversación o un encuentro, entre dos o más dispositivos de comunicación, o entre un ordenador y usuario.

Para ello en nuestro archivo main.py debemos alterar una key del dict app.config:

```py
# Armo mí secret key para ocultar los datos sensibles del usuario: 
app.config["SECRET_KEY"] = 'SUPER SECRETO' # Al pasar a production luego vamos a encriptar este dato que es lo correcto. 
```

Luego importo session desde flask:

```py
# Armo mí secret key para ocultar los datos sensibles del usuario: 
app.config["SECRET_KEY"] = 'SUPER SECRETO' # Al pasar a production luego vamos a encriptar este dato que es lo correcto. 
```

despues, dejo de guardar el user_ip en una cookie para guardarla dentro mi sesion: 

```py
@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello")) # Redirección guardada en variable
    # response.set_cookie("user_ip", user_ip) # Guardo IP en Cookie.
    session['user_ip'] = user_ip

    return response # Retornamos una respuesta de flask que en este caso es un redirect
```

finalmente, en la route "/hello" vamos a recuperar el user_ip de nuestra session en lugar de la cookie como veniamos haciendo:

```py
@app.route("/hello")
def hello():
    # user_ip = request.cookies.get("user_ip") # Tomo el dato de IP ya no desde remote_addr sino desde la cookie que guarde en la def de arriba
    user_ip = session.get("user_ip")
    context = {
        'user_ip': user_ip,
        'todos': todos, # Importante no olvidar la ultima coma en el dict para que expanda todas las variables.
    }
    return render_template('hello.html', **context) # Hello World Flask. tu IP es 127.0.0.1.
    # Los ** son para expandir el diccionario y transformarlo en variables sueltas. 
```

Al ver la cookie en el navegador vamos a encontrar la misma encriptada por lo que ya no es posible acceder a ese dato como antes. 

Entonces ya vimos el uso de dos helpers de flask. request, de donde podiamos por ejemplo obtener las cookies y ahora session que nos permite guardar info de forma segura. Flask cuenta con otros objetos/helpers con distintas utilidades que se pueden ver acá: 

<img src="./images/helpers_flask.PNG">

--------------------------------------------------

## Implementacion de Flask-Bootstrap y Flask-WTF

**Manejo de información que nos brinda el usuario mediante formularios**

Los formularios generan peticiones de tipo "POST". 

WTF = Wath the forms

1- Instalamos flask-WTF:

```bash
pip install flask-wtf
```
2- Importo FlaskForm:

```py
from flask_wtf import FlaskForm 
```

3- Creo una clase que va a extender a FlaskForm, heredandola:

```py
class LoginForm(FlaskForm):
    pass
```

4- Esta clase debe completarse con los fields o campos que debe tener el form. Los mismos se traen de wtforms.fields así:

```py
from wtforms.fields import StringField, PasswordField
```

5- Para validar que los campos del form vengan con la info que necesitamos debemos importar wtforms otro elemento mas: 

```py
from wtforms.validators import DataRequired
```
DataRequired solamente valida que el field no venga vacio. Pero hay otros validators que podemos traer como maximo de caracteres, min de caracteres, etc.

Tenemos todos estos validadores en el module de "validators": 

```py
__all__ = (
    "DataRequired",
    "data_required",
    "Email",
    "email",
    "EqualTo",
    "equal_to",
    "IPAddress",
    "ip_address",
    "InputRequired",
    "input_required",
    "Length",
    "length",
    "NumberRange",
    "number_range",
    "Optional",
    "optional",
    "Regexp",
    "regexp",
    "URL",
    "url",
    "AnyOf",
    "any_of",
    "NoneOf",
    "none_of",
    "MacAddress",
    "mac_address",
    "UUID",
    "ValidationError",
    "StopValidation",
)
```

6- Estos validadores se pasan dentro de la instanciación del field:

```py
# Class LoginForm que hereda de FlaskForm:
class LoginForm(FlaskForm):
    # Los forms tienen campos o field que deben llenarse:
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) # WTF va a manejar pertinentemente estos password. Es decir de forma segura.
    # Agregamos un validador de datos que también lo tiene WTF
```

7- Solo nos falta generar un botón para que el usuario envíe el formulario lo que se hace importando la clase SubmitField

```py
from flask_wtf import FlaskForm 
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Class LoginForm que hereda de FlaskForm:
class LoginForm(FlaskForm):
    # Los forms tienen campos o field que deben llenarse:
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) # WTF va a manejar pertinentemente estos password. Es decir de forma segura.
    # Agregamos un validador de datos que también lo tiene WTF
    # Agregamos un SubmitField como botón de envio:
    submit = SubmitField("Enviar")
```
8- Una vez que ya tenemos nuestro form podriamos importarlo dentro de nuestro archivo hello.html para que el usuario pueda enviarnos info. Para eso debemos enviar una instancia de nuestra clase LoginForm en el context del render_template para la path operation de "/hello" así: 

```py
@app.route("/hello")
def hello():
    # user_ip = request.cookies.get("user_ip") # Tomo el dato de IP ya no desde remote_addr sino desde la cookie que guarde en la def de arriba
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'todos': todos, # Importante no olvidar la ultima coma en el dict para que expanda todas las variables.
        'login_form': login_form,
    }
    return render_template('hello.html', **context) # Hello World Flask. tu IP es 127.0.0.1.
    # Los ** son para expandir el diccionario y transformarlo en variables sueltas. 
```

Y luego recibirla en el template HTML hello.html para renderiar el form usando bootstrap4 de esta manera: 

```html
<!-- Herencia de templates -->
{% extends 'base.html' %}
<!-- Import de macros para un render mas efectivo -->
{% import 'macros.html' as macros %}
<!-- Import de bootstrap a wtf para renderiar el form mas facil -->
{% from 'bootstrap4/form.html' import render_form %}

{% block title %}
    {{ super() }}
    Bienvenido
{% endblock title %}

{% block content %}
    <!-- Condicionales en template HTML -->
    {% if user_ip %}
        <h2>Hello World, tu Ip es {{user_ip}} </h2>
    {% else %}
        <a href="{{ url_for('index') }}">Ir a inicio</a>
    {% endif %}

    <!-- Class container viene desde Bootstrap-->
    <div class="container">
        <!-- 
        <form action="{{ url_for('hello') }}" method="POST">
            {{ login_form.username }}
            {{ login_form.username.label }}
            {{ login_form.password }}
            {{ login_form.password.label }}
            {{ login_form.submit }}
            {{ login_form.submit.label }}
        </form>
        -->
        {{ render_form(login_form) }}
    </div>

    <!-- Ciclo for en template HTML -->
    <ul>
        {% for todo in todos %}
            {{ macros.render_todo(todo) }}
        {% endfor %}    
    </ul>
    <!-- Prueba -->
    <h3>Hola</h3>
{% endblock content %}
```

Si no quisieramos renderiar el form usando bootstrap (de por si mas que recomendado) entonces podemos hacerlo también de forma tradicional con Jinja com el bloque de codigo que está comentado dentro de la div class= "container"

Ya no tenemos entonces nuestro form armado, pero si enviamos los datos nos aparecera un error dado que no estamos recibiendo los mismos en nuestro servidor

Error al enviar: 

**Method Not Allowed**
**The method is not allowed for the requested URL.**

-------------------------------------

## Uso de método POST en Flask-WTF

Flask acepta peticiones GET por defecto y por ende no debemos declararla en nuestras rutas.

Pero cuando necesitamos hacer una petición POST al enviar un formulario debemos declararla de la siguiente manera, como en este ejemplo:

```py
@app.route('/platzi-post', methods=['GET', 'POST'])
```

Debemos declararle además de la petición que queremos, GET, ya que le estamos pasando el parámetro methods para que acepte solo y únicamente las peticiones que estamos declarando.

De esta forma, al actualizar el navegador ya podremos hacer la petición POST a nuestra ruta deseada y obtener la respuesta requerida.

Para usar los datos de la petición POST debemos primero validar con un "if" si el formulario fue submiteado y en caso afirmativo recargar la pagina desde el index así: 

```py
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

        # Redirijo a index en caso de que completen el form:
        return redirect(url_for('index'))
    
    # Este return es para si nos hacen un "GET":
    return render_template('hello.html', **context) # Hello World Flask. tu IP es 127.0.0.1.
    # Los ** son para expandir el diccionario y transformarlo en variables sueltas. 
```

--------------------------------------------

## Desplegar Flashes (mensajes emergentes) con Flask:

1- Esto es posible gracias a la función "flash" de Flask. Por lo que primero debemos importarla así

```py
from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
```

2- Creamos nuestro flash en python de la siguiente manera: 

```py
# Guardo un flash en memoría que luego debo reenderiarlo en HTML:
flash('Nombre de usuario registrado con exito!')
```

3- Renderizamos nuestro/s mensajes en el template de la siguiente forma si estamos trabajando con Bootstrap5:

```html
            {% block flash %}
                {% with messages = get_flashed_messages() %}
                    {% if messages %}
                        {% for message in messages %}
                            <div class="alert alert-success alert-dismissible">
                                <button type="button" 
                                        data-bs-dismiss="alert" 
                                        class="close">&times;</button>
                                {{ message }}
                            </div>
                        {% endfor %}
                    {% endif %}
                {% endwith %}
            {% endblock  %}
```

Para que funcione la acción de cerrar el flash al presionar la "X" de nuestro button debemos primero importar en nuestro base.html los archivos JavaScript de Bootstrap5. 

Eso se hace con un block script en base.html de así: 

```html
            {% block scripts %}
                {{ bootstrap.load_js() }}
            {% endblock %}
```

--------------------------------

## Pruebas basicas con Flask-testing:

La etapa de pruebas se denomina testing y se trata de una investigación exhaustiva, no solo técnica sino también empírica, que busca reunir información objetiva sobre la calidad de un proyecto de software, por ejemplo, una aplicación móvil o un sitio web.

El objetivo del testing no solo es encontrar fallas sino también aumentar la confianza en la calidad del producto, facilitar información para la toma de decisiones y detectar oportunidades de mejora.

1- Instalamos flask-testing (aunque podriamos hacerlo directamente con unit-test de python):

```bash
pip install flask-testing
```

2- Creo un comando para que cuando ejecute flask test corra las pruebas que declare. En el file donde cree mi instancia de Flask (app) debo entonces hacer lo siguiente:

```py
# Creo mi comando para ejecutar las pruebas automatizadas al correr "flask test" en terminal:
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
```

Para hacer la función decorada de arriba necesito primero importar unittest

3- Creo una carpeta "tests" en la raiz de mi proyecto donde voy a guardar todas las pruebas automatizadas. 

4- Pruebo el comando flask test en consola. Si no funciona vuelvo a exportar el nombre de mi FLASK_APP:

```bash
export FLASK_APP=main.py
```

5- Al correr flask test no ejecutara ninguno dado que no creamos ningun test por el momento.

6- Creamos nuestro primer testeo: 

```py
from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest(TestCase):
    # Sobre escribo metodo de TestCase para crear instancia de la app que vo ya testear:
    def create_app(self):
        app.config['TESTING'] = True
        # Desactivamos el validador de formularios:
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    # Primer prueba (Verifica si hay una instancia de nuestro proyecto activo)
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    # Segunda prueba (Verifica que la app esté en ambiente de testing)
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    # Tercera prueba (Verifica que nuestro index redirija a Hello)
    def test_index_redirect(self):
        response = self.client.get(url_for('index'))

        # ¿Es cierto que la response a mi request get redirije a Hello? 
        self.assertEqual(response.location, '/hello')

    # Cuarta prueba (Probar que hello nos regresa status code 200 al hacer GET)
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))

        self.assert200(response)

    # Quinta prueba (Probar que hello funcione bien al hacer un post):
    def test_hello_post(self):
        fake_user = {
            "username":"Mariano Gobea Alcoba",
            "password": "lalala1234"
        }
        response = self.client.post(url_for('hello'), data=fake_user)

        # ¿Luego del post me redirige al index mi route "hello"?
        self.assertEqual(response.location, '/')
```

---------------------------------------

## App Factory: Module App en proyectos Python que sirve para crear una instancia de nuestra app. 

1- Se crea un module llamado "app" con un archivo llamado __init__.py

2- Allí se crea una function llamada create_app()

```py
from flask import Flask
from flask_bootstrap import Bootstrap5

from .config import Config

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)

    app.config.from_object(Config)

    return app
```
3- En el mismo modulo vamos a crear una class Config con la cual vamos a setear todos los elementos de configuración de nuestra 

```py
class Config:
    SECRET_KEY = 'SUPER SECRET'
```

4- Muevo static y templates al directorio app para que pueda encontrar los archivos cuando se ejecuta la app.

5- Voy a crear otro archivo llamado forms.py para mover allí mi clase LoginForm que hereda de "FlaskForm":

```py
from flask_wtf import FlaskForm 
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Class LoginForm que hereda de FlaskForm:
class LoginForm(FlaskForm):
    # Los forms tienen campos o field que deben llenarse:
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) # WTF va a manejar pertinentemente estos password. Es decir de forma segura.
    # Agregamos un validador de datos que también lo tiene WTF
    # Agregamos un SubmitField como botón de envio:
    submit = SubmitField("Enviar")
```

----------------------------------

## Uso de Blueprints:

**Blueprints**: son una serie de rutas que podemos integrar en nuestra aplicacion pero en otro directorio
es decir, me va a permitir modular la aplicación en pequeñas aplicaciones que hagan cosas específicas
como autenticación o la parte de welcome, o si tenemos un dashboard de tareas por ejemplo también
crearíamos un blueprint para las tareas específicas y es más fácil de manejar.

Son como **mini apps** dentro de mi app, con todos sus elementos propios y aislados. 

1. Creo un directorio dentro de app para cada blueprint. En este caso primero un directorio para "auth". 

2. Luego dentro del directorio creado voy a armar un __init__.py

```py
from flask import Blueprint

# Creo el blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')
# El prefijo significa que todas las rutas que comiencen con /auth van a redirigir a este blueprint

# Creo las vistas de este blueprint en un archivo que se llame views.py dentro del modulo
```

3. Creo un archivo views.py dentro de mi sub modulo "auth" con el siguiente contenido: 

```py
from flask import render_template

from app.forms import LoginForm
from . import auth


@auth.route('/login')
def login():
    context = {
        'login_form': LoginForm()
    }
    return render_template('login.html', **context)
```

4. Creo el template login.html que voy a renderiar desde mi auth.route: 

```py
<!-- Herencia de templates -->
{% extends 'base.html' %}
<!-- Import de bootstrap a wtf para renderiar el form mas facil -->
{% from 'bootstrap4/form.html' import render_form %}

{% block title %}
    {{ super() }}
    Login
{% endblock title %}

{% block content %}
    <div class="container">
        {{ render_form(login_form) }}
    </div>
{% endblock %}
```

**Blueprints**: Una serie de rutas que vamos a poder integrar en nuestra aplicación pero en otro directorio. Por ejemplo: "login", "welcome" o "dashboard de tareas". 

--------------------------------------

## Blueprints II

Excelente tutorial sobre blueprints (planos) en Flask: 

https://www.youtube.com/watch?v=3Yz6QanCSaA

1. Forma de simplificar una aplicacion de Flask
2. Es la forma de extender y factorizar nuestra aplicación
3. NO es una aplicación aparte de Flask
4. Cada blueprints va a tener todos los endpoints que necesite. 
5. Ejemplo: Una app con un file app.py donde se inicializa la web app y se crea un endpoint de entrada a la app. Luego debemos despues de crear la app asociar los distintos blueprints a nuestra app. Esto se puede hacer en app.py si es que allí inicializamos la app de Flask o en un archivo __init__.py que viva dentro de un module app y se una funcion para inicializar la app y configurarla y luego asignarle los blueprints correspondientes. 
6. Luego armo mis distintos blueprints. Puedo armar distintos archivos py con sus nombres o puedo armar distintos modulos, por ejemplo "auth" con archivos __init__.py y archivos views.py que sirvan para inicializar los blueprints y establecer sus visualizaciones en distintos endpoints

---------------------------------------

## Base de datos y App Engine con Flask

Flask no tiene un ORM o base de datos con la que trabaja por default. Por lo que podemos trabajar con la base de datos que nosotros queramos siempre que hagamos la configuración correcta de la misma. 

- **Bases de Datos SQL**: su composición esta hecha con bases de datos llenas de tablas con filas que contienen campos estructurados. No es muy flexible pero es el más usado. Una de sus desventajas es que mientras más compleja sea la base de datos más procesamiento necesitará.
Para trabajar con estas bases de datos Flask cuenta con SQLAlchemy como extensión apropiada para tales fines. 

- **Base de Datos NOSQL**: su composición es no estructurada, es abierta y muy flexible a diferentes tipos de datos, no necesita tantos recursos para ejecutarse, no necesitan una tabla fija como las que se encuentran en bases de datos relacionales y es altamente escalable a un bajo costo de hardware. 
Nosotros vamos a trabajar con una base de datos no relacional llamada Firebase. 
En este tipo de base de datos las tablas, rows, columns and primary keys de las bases de datos relacionales se la conoce de otra manera: 

- Table = Collection group
- Row = Document
- Column = Field
- Primary key = Document ID

Vamos a armar una estructura con dos Collection group: 

- Users
- To do´s

Ambos van a tener su propio ID: 

- User ID
- To do ID

Con ellos luego podemos recontruir que tareas son de cada usuario

------------------------------------------

## Firebase en Google Cloud Platform 

Para poder usar el CLI de gcloud (Google Cloud SDK) primero debes instalar su paquete instalador desde la pagina de Google Cloud. Luego una vez instalado autenticarte corriendo el comando: 

```bash
gcloud auth login
```
Aunque también funciona con: 

```bash
gcloud init
```

Si usaste el comando gcloud init te va a pedir que elijas un proyecto por defecto. Por ejemplo yo tengo para este trabajo un proyecto en gcloud llamado "mgobea-flask" ahora bien puede ocurrir que con la misma sesión en otro trabajo requieras cambiar el proyecto. Si eso ocurre puedes hacerlo con el siguiente comando: 

```bash
gcloud config set project PROJECT_ID
```

Luego debemos armar nuestra colección de usuarios declarando el primer documento o "caso" de usuario y dentro de este primer caso declarar una nueva coleccion en este caso de "todos" para también generar un primer documento o caso. 

Posteriormente para administrar estos documentos desde la consola debemos correr el comando: 

```bash
gcloud auth application-default login
```
Con este comando vamos a poder comunicarnos desde nuestro servidor local con la base de datos noSQL de Firebase.

-------------------------------------------------

## Implementación de Firestore:

1. Crear dentro del module "app" firestore_service.py
2. Importamos en nuestro venv "firebase-admin"
3. Armamos la config de firestore_service.py así:

```py
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
def get_users(): 
    return db.collection('users').get()
```

4. Importo y ejecuto la inicialización de database para obtener los users en main.py

```py
@app.route("/hello", methods=['GET'])
def hello():
    user_ip = session.get("user_ip")
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'username': username,
        'todos': todos, 
    }

    users = get_users() # Nos devuelve una lista de usuarios sobre la cual vamos a poder iterar

    for user in users:
        print(user.id)
        print(user.to_dict()['password']) # El print en este caso será por consola. No en el template.
    
    return render_template('hello.html', **context)
```
Ahí me estoy trayendo los usuarios pero puedo traer tambien los todos de mis usuarios directamente desde mi database para dejar de hardcodearlos...

1. Implemento un nuevo servicio/conexion llamado get_todos(user_id) en firestore_service.py para traer los "todos": 

```py
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
def get_users(): 
    return db.collection('users').get()

# Armo mi segunda función para esta vez traer mis todos de mi database Firebase: 
def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()
```

2. Recibo los todos dentro de mi context: 

```py
@app.route("/hello", methods=['GET'])
def hello():
    user_ip = session.get("user_ip")
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'username': username,
        'todos': get_todos(username),
    }

    users = get_users() 

    for user in users:
        print(user.id)
        print(user.to_dict()['password']) 

    return render_template('hello.html', **context)
```

3. En mi macro, donde renderizo mis todos, transformo los mismos a dict y le pido que actue solo sobre la key "description" para así evitar que me renderize la ubicación en memoria del objeto en lugar de mi descripción: 

```html
<!-- Macro que va a renderiar el contenido de mi lista -->
{% macro render_todo(todo) %}
    <li>Descripción: {{todo.to_dict().description}}</li> 
{% endmacro %}
```

Listo! Ya veo en mi web app las tareas de mi user "mariano". Traidas desde mi database noSQL (firebase). Luego debemos registrar los usuarios y las tareas en firebase directamente con el post de la app y no como lo hicimos nosotros desde Google Cloud. Pero esto viene despues... 

---------------------------------------

## Autenticación de usuarios: Login

**Flask Login**

Librería de Flask que nos permite buscar un usuario, identificar si existe, luego validar la contraseña y en caso de que todo este bien darle acceso al servicio. 

1. Borro el mostrar los usuarios por consola de mi path operation "/hello" dado que no lo voy a usar así...quedaría la path operation así: 

```py
@app.route("/hello", methods=['GET'])
def hello():
    user_ip = session.get("user_ip")
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'username': username,
        'todos': get_todos(username),
    }

    users = get_users() 

    return render_template('hello.html', **context)
```

2. Instalamos la libreía flask-login en nuestro venv: 

```bash
pip install flask-login
```

3. Importamos la librería en nuestro archivo de __init__.py del module "app", inicializamos un objeto login_manager y le indicamos la ruta a gerenciar así como que app debe gerenciar

```py
# Importaciones de Flask y sus librerías: 
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

# Importo mi Config para luego configurar con ella mi app: 
from .config import Config
# Importo mi blueprint para poder registrarlo luego en app:
from .auth import auth

# Instanceo un obejto LoginManager
login_manager = LoginManager()
# Le explicito a mi objeto sobre que route va a a trabajar: 
login_manager.login_view = 'auth.login'

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
```

4. Hecho esto, vamos a ponerle un decorador propio de LoginManager a la route que queremos que gerencie

Primero lo importamos al decorador así:

```py
from flask_login import login_required
```

Luego lo usamos así: 

```py
@app.route("/hello", methods=['GET'])
@login_required
def hello():
    user_ip = session.get("user_ip")
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'username': username,
        'todos': get_todos(username),
    }

    users = get_users() 

    return render_template('hello.html', **context)
```

5. Para evitar en la nueva versión de flask-login el error "Missing user_loader or request_loader error" se debe importar en nuestro "firestore_service.py" el objeto instanciado de nuestro LoginManager para usarlo como decorador arriba de la def get_users() así: 

```py
from . import login_manager

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
@login_manager.user_loader # Decorador que traigo de mi objeto login_manager para evitar error "Missing user_loader or request_loader"
def get_users(): 
    return db.collection('users').get()

# Armo mi segunda función para esta vez traer mis todos de mi database Firebase: 
def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()
```

Esto ya evitara que podamos acceder a "/hello" (alli pusimos el decorador) sin antes haber realizado un logín en la ruta que el login_manager está gerenciando( Así lo declaramos en el atributo login_view luego de instanciar nuestro login manager). De hecho hasta imprimirá un mensaje en el template que indica que "Please log in to access this page"

6. Implementamos nuestro user_model. El mismo lo vamos a hacer en un nuevo archivo dentro de nuestro module "app" al cual llamaremos "models.py"

```py
from .firestore_service import get_user

from flask_login import UserMixin

class UserData():
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserModel(UserMixin): 
    def __init__(self, user_data: UserData):
        """
        :param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod # Indica que es un metodo estatico. Es decir, no recibe self. 
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(
            username = user_doc.id,
            password = user_doc.to_dict()['password']
        )

        return UserModel(user_data)
```

7. Implemento el metodo get_user(user_id) en mi firestore y dejo de usar el decorador de mi login_manager acá para pasar a usarlo en mi __init__.py

```py
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
```
8. Implemento en __init__.py de app la func load_user():

```py
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
```

Ahora debemos verificar que el usuario que está ingresando esté en nuestra base de datos y caso afirmativo darle acceso...

------------------------------------------------






















