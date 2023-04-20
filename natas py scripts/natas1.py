#!/usr/bin/env python

# import the package requests which is for html information
import requests
import re

username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.get(url,auth = (username, password))
content = response.text

# print(content)

print(re.findall('<!--The password for natas2 is (.*) -->', content)[0])