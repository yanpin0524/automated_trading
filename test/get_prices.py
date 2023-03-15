import requests
import json
from decouple import config

profile = {
  "identifier": config('identifier'),
  "password": config('password'),
  'X-CAP-API-KEY': config('X-CAP-API-KEY')
}


basic_url = 'https://demo-api-capital.backend-capital.com/api/v1'

payload = json.dumps({
  "identifier": profile['identifier'],
  "password": profile['password']
})

headers = {
    'X-CAP-API-KEY': profile['X-CAP-API-KEY'],
    'Content-Type': 'application/json'
}


res = requests.post(url=basic_url + '/session', data=payload, headers=headers)
res_content = res.content.decode('utf-8')
res_header = res.headers