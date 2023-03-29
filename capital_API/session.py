import requests
import json

basic_url = 'https://demo-api-capital.backend-capital.com/api/v1'

def create_new_session(identifier, password, API_KEY):
    payload = json.dumps({
        "identifier": identifier,
        "password": password
    })

    headers = {
        'X-CAP-API-KEY': API_KEY,
        'Content-Type': 'application/json'
    }

    return requests.post(url='{}/session'.format(basic_url), data=payload, headers=headers)


def logout_session(token, cst):
    headers = {
        'X-SECURITY-TOKEN': token,
        'CST': cst
    }

    return requests.delete(url='{}/session'.format(basic_url), headers=headers)