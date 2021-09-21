#!/usr/bin/env python3
import cgi, secret, templates, os

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

login = "LoggedIn=False"
if (username == secret.username and password == secret.password):
    login = "LoggedIn=True"

print(f"Set-Cookie:{login};\r")
print("Content-type:text/html\r\n\r\n")
print()

print("<html>")
print("<head>")
print("<title>afterlogin.py</title>")
print("</head>")
print("<body>")

# fixes cookie sync issue (having to refresh to get current cookie instead of previous cookie)
if (os.environ['HTTP_COOKIE'] != login): # if cookies are not synced with real time yet
    if (os.environ['HTTP_COOKIE'] == "LoggedIn=False"): # use reverse logic
        print(templates.secret_page(username, password))
    else:
        print(templates.after_login_incorrect())
else:
    if (os.environ['HTTP_COOKIE'] == "LoggedIn=True"): # use normal logic
        print(templates.secret_page(username, password))
    else:
        print(templates.after_login_incorrect())

print("</body>")
print("</html>")
