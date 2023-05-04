from flask import Flask, redirect, session, url_for, render_template, request
import random
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def generate(email):
    otp = ''.join([str(random.randint(0,9)) for i in range(6)])
    password = 'dtvslhyhmhsmuiht'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ishitagopal98@gmail.com', password)
    msg = 'Hello, your otp is ' + str(otp)
    print(otp)
    server.sendmail('ishitagopal98@gmail.com', email, msg)
    print("sent!")
    server.quit()
    return otp

otObtained = 0

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])

def index():

    return render_template('index.html')

@app.route('/otp_ui', methods=["POST", "GET"])

def otp_ui():
    global otObtained
    name = request.form['name']
    choices = request.form.get("options_select")
    # print(choices)
    if(choices=="option1"):
        email = request.form['email']
        otObtained = generate(email)
        return render_template('otp_ui.html')
    else:
        phone = request.form['phone']
        otObtained = generate_phone(phone)
        return render_template('otp_ui.html')

def generate_phone(contact):
    OTP=random.randint(100000,999999)
    client=Client()
    account_sid=os.getenv("TWILIO_ACCOUNT_SID")
    auth_token=os.getenv("TWILIO_AUTH_TOKEN")
    client=Client(account_sid,auth_token)

    message=client.messages.create(
        body="Your OTP is "+str(OTP), from_="+19783961781",to=contact
        )
    # print(OTP)
    return OTP

@app.route('/nextPage', methods=["POST", "GET"])
def nextPage():
    msg = ""
    ot0 = int(request.form["otp0"]) * 100000
    ot1 = int(request.form["otp1"]) * 10000
    ot2 = int(request.form["otp2"]) * 1000
    ot3 = int(request.form["otp3"]) * 100
    ot4 = int(request.form["otp4"]) * 10
    ot5 = int(request.form["otp5"]) * 1
    
    ot = ot0 + ot1 + ot2 + ot3 + ot4 + ot5
    print(ot)
    if(ot==int(otObtained)):
        return render_template('nextPage_Verified.html')
    else:
        return render_template('nextPage_Failed.html')

    # return render_template('nextPage.html', msg = msg)

@app.route('/', methods=["POST", "GET"])
def backHome():
    render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)