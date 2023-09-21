import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_URL = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"


def get_weather(lat: float, lon: float) -> str:
    response = requests.get(
        WEATHER_API_URL.format(lat=lat, lon=lon, api_key=os.getenv("WEATHER_API_KEY"))
    )
    return json.dumps(response.json())
