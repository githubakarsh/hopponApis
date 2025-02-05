from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<div>Hello world !!</div>"

@app.route("/index")
def index():
    return "Index page data"

@app.route("/home")
def home():
    return "Home page data"

@app.route("/<name>")
def notFoundPage(name):
    return f"the page {escape(name)} doesnot exist"

@app.route("/generate-random/<number>")
def generateRandomKey(number):
    newNumber = int(number)
    randomNum = newNumber+1*2
    return f"random number generated - {randomNum}"


