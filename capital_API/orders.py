import requests
import json

basic_url = 'https://demo-api-capital.backend-capital.com/api/v1'


def create_position(headers, epic, direction, size, stop=None, profit=None):
    headers['Content-Type'] = 'application/json'

    payload = {
        "epic": epic,
        "direction": direction,
        "size": size
    }

    if stop:
        payload.update(stop)
    if profit:
        payload.update(profit)

    return requests.post(url='{}/positions'.format(basic_url), data=json.dumps(payload), headers=headers)
