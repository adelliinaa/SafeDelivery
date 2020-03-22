import requests
from flask import Flask, request
from twilio import twiml
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


#@app.route("/voice", methods=['GET', 'POST'])
#def voice():
"""Respond to incoming phone calls with a 'Hello world' message"""
#    # Start our TwiML response
#    city = request.values['FromCity']

"""  if not request.values['RecordingStatus'] and not request.values['RecordingUrl']:
        # Start our TwiML response
        resp = VoiceResponse()

        # Read a message aloud to the caller
        resp.say('Hello. Welcome to Goodiebox, your shopping assistant. We will help you remain in a safe \
                 environment by pairing your order with a volunteer which will run the errands for you. \
                 The first thing we will need is your name, please talk slowly and press on number 5 on your \
                 phone keyboard once you are done.', voice="alice")

        resp.record(action="/voice",
                    timeout=20,
                    transcribe=True)

        return str(resp)

    elif request.values['RecordingStatus'] == "completed":
        resp = VoiceResponse()
        resp.say('You said:', voice="alice")
        resp.play(request.values['RecordingUrl'])
        resp.hangup()
        return str(resp)

    else:
        resp = VoiceResponse()
        resp.pause(length=10)
        resp.redirect(url="/voice")
        return str(resp)
"""

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    resp = VoiceResponse()

    resp.say('Hello. Welcome to Goodiebox, your shopping assistant. \
                     The first thing we will need is your name, please talk slowly and press on number 5 on your \
                     phone keyboard once you are done.', voice="alice")

    resp.pause(3)
    resp.say('The recorded name is Victor Stoian, is this correct? Press star if yes and 0 if you want to repeat')

    resp.pause(3)
    resp.say('What is your address')

    resp.pause(3)
    resp.say('The recorded address is: this is an address, is this correct? Press star if yes and 0 if you want to repeat')

    resp.pause(3)
    resp.say('What is your order?')

    resp.pause(5)
    resp.say('The recorded order is: flour, eggs and apples, is this correct?Press star if yes and 0 if you want to repeat')

    resp.pause(3)
    resp.say('Your order has been placed, we will notify you as soon as a volunteer accepts it, thank you for your patience')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1234)
