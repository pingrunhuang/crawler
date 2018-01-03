import requests

params = {"uername":"Frank", "password": "password"}

r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)

print("Cookie is set to:")
print(r.cookies.get_dict())
print("-----------")
print("Going to profile page...")
# way to send requests with cookies but just for one time
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)

# deal with the problem that the cookie changed a lot
# this method will keep track on the cookie 
s=session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)

# http basic access authentication
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('frank', 'password')
r = requests.post(url=" http://pythonscraping.com/pages/auth/login.php ", 
    auth=auth)
print(r.text)