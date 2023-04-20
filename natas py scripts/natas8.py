#!/usr/bin/env python

# PHP Base64 & Hex

# import the package requests which is for html information
import requests
import re

username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'

# url = 'http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8' % username
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# blank temp response = requests.get(url,auth = (username, password))

response = session.post(url,data = {"secret" : "oubWYf2kBq", "submit" : "submit" },auth = (username, password))
content = response.text

# print(content)
# (.*)

print(re.findall("The password for natas9 is (.*)", content)[0])