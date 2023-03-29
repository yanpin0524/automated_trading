import requests

basic_url = 'https://demo-api-capital.backend-capital.com/api/v1'


def get_prices(headers, epic='US100', resolution='', quantity=10, start_date='', end_date=''):
    params = {
        'resolution': resolution,
        'max': quantity,
    }

    if(start_date):
        params['from'] = start_date
    if(end_date):
        params['to'] = end_date

    return requests.get(url='{}/prices/{}'.format(basic_url, epic), headers=headers, params=params)
