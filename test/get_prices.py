import requests
import json
import os
#TODO: I change dotenv to python-dotenv  because I use conda to install packages, so might need to fix few code.
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

profile = {
    "identifier": os.getenv('identifier'),
    "password": os.getenv('password'),
    'X-CAP-API-KEY': os.getenv('X-CAP-API-KEY')
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


res_session = requests.post(
    url='{}/session'.format(basic_url), data=payload, headers=headers)
res_content = res_session.content.decode('utf-8')
res_header = res_session.headers

if __name__ == '__main__':
    cst = res_header["CST"]
    security_token = res_header["X-SECURITY-TOKEN"]
    params = {
        'resolution': 'DAY'
    }

    try:
        res_market = requests.get(url='{}/prices/US100'.format(basic_url), params=params,
                                  headers={'X-SECURITY-TOKEN': security_token,   'CST': cst})

        market_content = res_market.json()

        data = pd.DataFrame(market_content['prices'])
        print(data)

    except Exception as err:
        print('error: {}'.format(err))
