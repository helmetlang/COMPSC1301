#!/usr/bin/env python

# PHP XOR

# import the package requests which is for html information
import requests
import re
import urllib
import base64


username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'

url = 'http://%s.natas.labs.overthewire.org/' % username


# blank temp response = requests.get(url,auth = (username, password))

session = requests.Session()
cookies = { "data": "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz"}
response = session.get(url,auth = (username, password), cookies = cookies)

content = response.text

cookie_data = session.cookies['data']
decoded_data = base64.b64decode(urllib.parse.unquote(cookie_data))
hex_encoded_data = decoded_data.decode('utf-8').encode('utf-8').hex()

# print(content)

# print(base64.b64decode(urllib.parse.unquote(session.cookies['data'])))
# (.*)

print(re.findall("The password for natas12 is (.*)<br>", content)[0])