#!/usr/bin/env python3
import templates
print("Content-type:text/html\r\n\r\n")
print()

def login_page():
    """
    Returns the HTML for the login page.
    """

    return templates._wrapper(r"""
    <h1> Welcome! </h1>

    <form method="POST" action="afterlogin.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """)

print("<html>")
print("<head>")
print("<title>login.py</title>")
print("</head>")
print("<body>")

print(login_page())

print("</body>")
print("</html>")
