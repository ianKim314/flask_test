from flask import Flask
#2
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#2
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

