#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os
import json
import secret
from http.cookies import SimpleCookie


form_ok = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

cookie_ok = cookie_username == secret.username and cookie_password == secret.password
if cookie_ok:
    username = cookie_username
    password = cookie_password

if form_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

#Q5 Set-Cookie

#Q6 HTTP_COOKIE

# Q4: gets the data via these fields
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

print("Content-Type: text/html")
print(0)

if not username and not password:
    print(login_page())

elif username == secret.username and password==secret.password:
    print(secret_page(username, password))
else:
    print(login_page())
    print("Username & password: ", username, password)


# Q7 Cookies are used for storing user data when browsing

