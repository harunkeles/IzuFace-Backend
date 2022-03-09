import requests
import json
import time
import os
from izu_face_manager.settings import BASE_DIR

url = 'https://api.openweathermap.org/data/2.5/weather?q=K%C3%BC%C3%A7%C3%BCk%C3%A7ekmece&lang=tr&appid=c6951d8c03cf8b12b18547e9d46e2128'

def get_one_hour_weather_info():
    req = requests.get(url)
    data =  json.loads(req.text)
    print(data)

    with open(os.path.join(BASE_DIR,'apiApp\\api\\weatherApi\\weather.json'), 'w') as json_file:
        json.dump(data, json_file) 

    time.sleep(1200)
    return get_one_hour_weather_info()

get_one_hour_weather_info()
