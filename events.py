
from flask import Flask
from markupsafe import escape
from flask_cors import CORS

events = Flask(__name__)
CORS(events);

@events.route("/create-event", methods=['GET'])
def createevent():
    return "create event"

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