import requests
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN')
owner = "marwahmanbir"
repo = "OpenEDU"
query_url = f"https://api.github.com/repos/marwahmanbir/OpenEDU/issues"
params = {
    "state": "open",
}
headers = {'Authorization': f'token 13c287fc6fd45c8f38802a1709c55f3bee4ca4a5'}
r = requests.get(query_url, headers=headers, params=params)
pprint(r.json()) 