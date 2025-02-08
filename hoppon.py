from flask import Flask

app = Flask(__name__)

@app.route("/login")
def userLogin():
    return f"logged in"

@app.route("/signup")
def userSignup():
    return f"sign up"

@app.route("/logout/<userId>")
def userLogout(userId):
    return f"logout successful {userId}"

