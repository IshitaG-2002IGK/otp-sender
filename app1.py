from flask import Flask, redirect, session, url_for, render_template, request
import random
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

def generate(contact):
    OTP=random.randint(1000,9999)
    client=Client()
    account_sid=os.getenv("TWILIO_ACCOUNT_SID")
    auth_token=os.getenv("TWILIO_AUTH_TOKEN")
    client=Client(account_sid,auth_token)

    message=client.messages.create(
        body="Your OTP is "+str(OTP), from_="+19783961781",to=contact
        )
    # print(OTP)
    return OTP
otObtained = 0

@app.route('/', methods=["POST", "GET"])

def index():

    return render_template('index.html')

@app.route('/otp', methods=["POST", "GET"])

def otp():
    global otObtained
    name = request.form['name']
    contact = request.form['contact']
    otObtained = generate(contact)
    print("otobtained: "+str(otObtained))
    return render_template('otp.html')

@app.route('/nextPage', methods=["POST", "GET"])
def nextPage():
    msg = ""
    ot = request.form["otp"]

    if(int(ot)==otObtained):
        msg = "Verification Successful!"
    else:
        msg = "Not the right OTP! mk"

    return render_template('nextPage.html', msg = msg)


if __name__ == "__main__":
    app.run(debug=True)
