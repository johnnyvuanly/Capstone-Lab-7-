import os
import requests
from pprint import pprint
from datetime import datetime

key = os.environ.get('WEATHER_KEY')
query = {'q': 'Minneapolis, us', 'units': 'imperial', 'appid': key}

url = 'http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()
pprint(data)

list_of_forcasts = data['list']

for forecast in list_of_forcasts:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f'At {forecast_date} the temperature will be {temp}F')

""" I plan to keep using UTC time because it is more common and easier to convert to human readable time or whatever you want. More easier to change to what you want. """