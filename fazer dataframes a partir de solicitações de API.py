import datetime
import pandas as pd
import requests
import json



yesterday = datetime.date.today() - datetime.timedelta(days=1)

api = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
payload = {'format':'geojson',
            'starttime':yesterday - datetime.timedelta(days=26),
            'endtime':yesterday}

response = requests.get(api, params=payload)

earthquake_json = response.json()
#print(earthquake_json.keys())

#print(earthquake_json['metadata'])

#print(type(earthquake_json['features']))

dataset = [quake['properties'] for quake in earthquake_json['features']]

#print(dataset)

dataset = pd.DataFrame(dataset)

print(dataset.head())


