from flask import Blueprint, request
from key import API_KEY
import requests, json

api = Blueprint('api', __name__)

WEATHER_API = "https://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q="

@api.route('/api/weather')
def weather():
    args = request.args
    zipCode = args['z']
    if len(args) == 1:
        r = requests.get(url = WEATHER_API + zipCode)
        return r.json()
    else:
        return json.loads('{"error_msg": "location missing"}')