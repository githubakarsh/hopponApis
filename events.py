
from flask import Flask, request, make_response, jsonify
from markupsafe import escape
from flask_cors import CORS
from .utils.validateUserSignupDetails import validateUserSignupDetails
from .utils.classConstructors.createUserClass import User

events = Flask(__name__)
CORS(events)

@events.route("/create-user", methods=['POST'])
def createevent():
    signup_details = request.get_json()
    user = User(email=signup_details['email'], phone_number=signup_details['phoneNumber'], password=signup_details['password'], reset_password=signup_details['resetPassword'])
    print(signup_details)
    user_validator = validateUserSignupDetails(user)
    response = make_response('response',user_validator)
    return response
@events.route("/delete-event")
def deleteEvent():
    return "delete event"

@events.route("/modify-event-name/<eventId>")
def modifyEventName(eventId):
    return f"modifying event name of event id : {eventId}"

@events.route("/subscribe/<eventId>")
def subscribeToEvent(eventId):
    return f"subscribe to event with event id : {eventId}"

@events.route("/unsubscribe/<eventId>")
def unsubscribeEvent(eventId):
    return f"unsubscribe to event with event id: {eventId}"

@events.route("/like/<eventId>")
def likeEvent(eventId):
    return f"like the event with event id : {eventId}"

@events.route("/unlike/<eventId>")
def unlikeEvent(eventId):
    return f"unlike the event with event id : {eventId}"

@events.route("/share/<eventId>")
def shareEvent(eventId):
    return f"share the event wit event id {eventId}"

@events.route("/comment/<eventId>", methods=['POST'])
def commentAevent(eventId):
    return f"comment the event with event id {eventId}"

@events.route("/addImages/<eventId>")
def addImagesToEvent(eventId):
    return f"add images to event id {eventId}"

@events.route('/get-events')
def getEvents():
    return []