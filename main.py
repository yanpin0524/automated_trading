import capital_API.session as API_session
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

res = API_session.create_new_session(
    profile['identifier'], profile['password'], profile['API_KEY'])

pp.pprint(res.json())

token = res.headers['X-SECURITY-TOKEN']
cst = res.headers['CST']

