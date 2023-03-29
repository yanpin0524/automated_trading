import requests
import json
from decouple import config
import pandas as pd
from IPython.display import display

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


res_session = requests.post(url='{}/session'.format(basic_url), data=payload, headers=headers)
res_content = res_session.content.decode('utf-8')
res_header = res_session.headers

if __name__ == '__main__':
  cst = res_header["CST"]
  security_token = res_header["X-SECURITY-TOKEN"]
  params = {
    'resolution': 'DAY'
  }

  try:
    res_market = requests.get(url='{}/prices/US100'.format(basic_url), params=params, headers={'X-SECURITY-TOKEN': security_token,   'CST': cst })

    market_content = res_market.json()

    data = pd.DataFrame(market_content['prices'])
    display(data)

  except Exception as err:
    print('error: {}'.format(err))