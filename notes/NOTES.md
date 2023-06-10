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

1- Esto es posible gracias a la clase "flash" de Flask. Por lo que primero debemos importarla así

```py
from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
```

2- 






