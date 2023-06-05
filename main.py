from flask import Flask

app = Flask(__name__) # Le paso como nombre el nombre de este archivo.

@app.route("/")
def hello():
    return "Hello World Fl"