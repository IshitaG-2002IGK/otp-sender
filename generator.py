import random
import smtplib

otp = ''.join([str(random.randint(0,9)) for i in range(4)])

password = 'hfqkzjryvrxigwzt'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('hari02maha@gmail.com', password)
msg = 'Hello, your otp is ' + str(otp)
print(otp)
server.sendmail('hari02maha@gmail.com', 'hari02maha@gmail.com', msg)
print("sent!")
server.quit()