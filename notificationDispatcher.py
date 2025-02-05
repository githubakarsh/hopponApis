

from flask import Flask

notif_dispatch = Flask(__name__)

@notif_dispatch.route('/sendNotifications/<userUniqueId>')
def sendNotifications(userUniqueId):
    # send the notifications to the user - use notification hub for the triggering the notifications - in app notifications
    return f"sent notifications for {userUniqueId}"