import smtplib

email = "hullinger.brad@gmail.com"
password = "PASSWORD"
email2 = "hullinger.brad@gmail.com"
message = "Choose message to send"

#Host "gmail" rejects the correct password so smtplib package does connect to SMTP
server = smtplib.SMTP(host="smtp.gmail.com", port=587)
server.starttls()
server.login(email, password)
server.sendmail(email, email2, message)
server.quit()