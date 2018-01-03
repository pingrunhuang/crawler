import urllib.request import urlopen
from bs4 import BeautifulSoup
import time

_from = "test@123.com"
_to="dst@321.com"
_msg="It is christmas today!"

def send_email(FROM, TO, MSG, STMP_SERVER='localhost'):
    import smtplib
    from email.mime.text import MIMEText
    msg = MIMEText(MSG)
    msg['From']=FROM
    msg['To']=TO
    sender = smtplib.SMTP(STMP_SERVER)
    sender.send_message(msg)
    sender.quit()

if __name__ == "__main__":
    # equivalent to requets.get("https://isitchristmas.com/")
    req = urlopen("https://isitchristmas.com/")
    bsObj = BeautifulSoup(req)
    # should check the language here
    while bsObj.find('a', attrs={'id':'answer'}).attrs['title'] == '不是':
        print("Not christmas yet")
        time.sleep(3600)
    
    send_email(_from, _to, _msg)

    
