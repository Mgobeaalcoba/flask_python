from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__) # Le paso como nombre el nombre de este archivo.

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello")) # Redirección guardada en variable
    response.set_cookie("user_ip", user_ip) # Guardo IP en Cookie.

    return response # Retornamos una respuesta de flask que en este caso es un redirect

@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip") # Tomo el dato de IP ya no desde remote_addr sino desde la cookie que guarde en la def de arriba
    return render_template('hello.html', user_ip=user_ip) # Hello World Flask. tu IP es 127.0.0.1.

