

from flask import Flask

user_f = Flask(__name__)

@user_f.route("/login", methods=['POST'])
def login():
    # make user login by getting email and password in encryption
    return f"logged in successfully"


@user_f.route("/logout/<userUniqueId>")
def logout(userUniqueId):
    #make the user to logout
    return f"logout successful for {userUniqueId}"

@user_f.route("/userProfile/<userUniqueId>", methods=['GET'])
def get_User_Profile(userUniqueId):
    #send the user profile details with the permission the user has
    return f"user proflie for {userUniqueId} has been sent successful"

@user_f.route("/signup", methods=['POST'])
def userSignup():
    return f"user sign up successful"


