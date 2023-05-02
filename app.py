from flask import Flask, redirect, session, url_for, render_template, request
import random
import smtplib
# from twilio.rest import Client
# from dotenv import load_dotenv
# import os

# from dotenv import load_dotenv


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
    email = request.form['email']
    otObtained = generate(email)
    return render_template('otp_ui.html')

# def generate(contact):
#     OTP=random.randint(1000,9999)
#     client=Client()
#     account_sid=os.getenv("TWILIO_ACCOUNT_SID")
#     auth_token=os.getenv("TWILIO_AUTH_TOKEN")
#     client=Client(account_sid,auth_token)

#     message=client.messages.create(
#         body="Your OTP is "+str(OTP), from_="+19783961781",to=contact
#         )
#     # print(OTP)
#     return OTP

@app.route('/nextPage', methods=["POST", "GET"])
def nextPage():
    msg = ""
    ot = request.form["otp"]
    if(ot==otObtained):
        msg = "Verification Successful!"
    else:
        msg = "Not the right OTP!"

    return render_template('nextPage.html', msg = msg)


if __name__ == "__main__":
    app.run(debug=True)