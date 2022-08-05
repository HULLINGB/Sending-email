import smtplib

email = "example@gmail.com"
password = "PASSWORD"
message = "Choose message to send"

server = smtplib.SMTP(host="smtp.gmail.com", port=587)
server.starttls()
server.login(email, password)
server.sendmail(email, email, message)
server.quit()