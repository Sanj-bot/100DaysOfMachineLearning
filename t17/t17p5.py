import requests
import json
response_API = requests.get('https://gmail.googleapis.com/gmail/v1/users/sanjaygurjar741@gmail.com/profile')
print(response_API.status_code)

