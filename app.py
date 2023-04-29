from flask import Flask, redirect, session, url_for, render_template, request
import random
import smtplib
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

otObtained = 0;

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])

def index(): 
    
    return render_template('index.html')

@app.route('/otp', methods=["POST", "GET"])

def otp():
    global otObtained
    name = request.form['name']
    email = request.form['email']
    otObtained = generate(email)
    return render_template('otp.html')

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