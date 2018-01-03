import smtplib
from email.mime.text import MIMEText

_from="test@123.com"
_to="pingrunhuang@yahoo.com"

msg=MIMEText("Hello world!!!!!!!")

msg["From"]=_from
msg["To"]=_to
msg["Subject"]="Alert email"

s=smtplib.SMTP("localhost")
s.send_message(msg)
s.quit()