import smtplib
from settings import *


server = smtplib.SMTP(host=host,port=port)
server.login(sender, password)
server.sendmail(sender, receiver, message)
print("Email sent")
