from capital_API import session
from capital_API import prices
from capital_API import orders
import os
from dotenv import load_dotenv
from pprint import PrettyPrinter
import json

load_dotenv()
pp = PrettyPrinter(indent=2)

profile = {
    "identifier": os.getenv('identifier'),
    "password": os.getenv('password'),
    "API_KEY": os.getenv('X-CAP-API-KEY')
}

res = session.create_new_session(
    profile['identifier'], profile['password'], profile['API_KEY'])

headers = {
    'X-SECURITY-TOKEN': res.headers['X-SECURITY-TOKEN'],
    'CST': res.headers['CST']
}

# res2 = prices.get_prices(headers, 'USDJPY', 'HOUR_4')
# pp.pprint(res2.json())

stop = {
    'trailingStop': True,
    'stopDistance': 15
}
res3 = orders.create_position(headers, 'USDJPY', 'BUY', 1000, stop)
pp.pprint(res3.json())
