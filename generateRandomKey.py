from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/generatePassword/<inputemail>")
def generatePassword(inputemail):
    return f"{inputemail}"