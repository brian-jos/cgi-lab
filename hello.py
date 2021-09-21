#!/usr/bin/env python3
import os
print("Content-type:text/html\r\n\r\n")
print()

print("<html>")
print("<head>")
print("<title>hello.py</title>")
print("</head>")
print("<body>")

print(f"<p>{os.environ}</p>")
print(f"<h2>QUERY_STRING: {os.environ['QUERY_STRING']}</h2>")
print(f"<h2>HTTP_USER_AGENT: {os.environ['HTTP_USER_AGENT']}</h2>")
print("<a href='login.py'> To log in. </a>")

print("</body>")
print("</html>")
