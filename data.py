import requests
from pprint import pprint

query = {'locations': None, 'date': None, 'qualities': None, 'time-scale': None}
r = requests.get('https://albion-online-data.com/api/v2/stats/Charts/T5_LEATHER', params=query)
pprint(r.json()[0])