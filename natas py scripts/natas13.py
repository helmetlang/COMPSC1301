#!/usr/bin/env python

# had to do with burpsuite

# import the package requests which is for html information
import requests
import re


username = 'natas13'
password = 'lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9'

url = 'http://%s.natas.labs.overthewire.org/' % username

# blank temp response = requests.get(url,auth = (username, password))
session = requests.Session()

response = session.get(url,auth = (username, password))

content = response.text
print(content)
# (.*)

# print(re.findall("The password for natas12 is (.*)<br>", content)[0])


# natas 13 qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP