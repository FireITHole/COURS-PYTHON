import requests
from yaml import safe_load
from datetime import datetime
from json import dumps, loads

# URL Doc API Géolocalisation : https://openweathermap.org/api/geocoding-api

with open("secret.yaml") as file:
    SECRETS = safe_load(file)

GEOLOC_API_KEY = SECRETS["api_key"]
CITY = SECRETS["ville"]
DB_FILE = "db.json"


class Weather:
    def __init__(self, city: str):
        self.city = city
        weather_data, weather_units = self.get_weather_data(city)
        self.time: datetime = datetime.fromisoformat(weather_data["time"])
        self.temperature = weather_data["temperature_2m"]
        self.temperature_unit = weather_units["temperature_2m"]
        self.humidity = weather_data["relativehumidity_2m"]
        self.humidity_unit = weather_units["relativehumidity_2m"]
        self.apparent_temp = weather_data["apparent_temperature"]
        self.apparent_temp_unit = weather_units["apparent_temperature"]
        self.precipitation = weather_data["precipitation"]
        self.precipitation_unit = weather_units["precipitation"]
        self.windspeed = weather_data["windspeed_10m"]
        self.windspeed_unit = weather_units["windspeed_10m"]

    def __repr__(self) -> str:
        return f"Météo pour la ville de {self.city} à {self.time.strftime('%Hh%M')} GMT :\n\
    - Température : {self.temperature}{self.temperature_unit}\n\
    - Humidité : {self.humidity}{self.humidity_unit}\n\
    - Température apparente : {self.apparent_temp}{self.apparent_temp_unit}\n\
    - Précipitation : {self.precipitation}{self.precipitation_unit}\n\
    - Vitesse du vent : {self.windspeed}{self.windspeed_unit}"

    def get_weather_data(self, city: str) -> (dict, dict):
        GEOLOC_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={GEOLOC_API_KEY}"
        geoloc_res = requests.get(GEOLOC_URL)
        geoloc_res = geoloc_res.json()

        LAT = geoloc_res[0]["lat"]
        LON = geoloc_res[0]["lon"]

        WEATHER_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,windspeed_10m"
        weather_res = requests.get(WEATHER_URL)
        weather_res = weather_res.json()

        return (weather_res["current"], weather_res["current_units"])

    def get_city(self) -> str:
        return self.city

    def get_time(self) -> datetime:
        return self.time

    def get_temperature(self) -> float:
        return self.temperature

    def get_humidity(self) -> int:
        return self.humidity

    def get_apparent_temperature(self) -> float:
        return self.apparent_temp

    def get_precipitation(self) -> float:
        return self.precipitation

    def get_windspeed(self) -> float:
        return self.windspeed

    def register_data(self, db_file: str) -> None:
        with open(db_file) as file:
            db_data: list = loads(file.read())

        model = {
            self.time.strftime("%d/%m/%Y-%Hh%M"): {
                "city": self.city,
                "data": {
                    "temperature": self.temperature,
                    "humidity": self.humidity,
                    "apparent_temp": self.apparent_temp,
                    "precipitation": self.precipitation,
                    "wind_speed": self.windspeed,
                },
                "units": {
                    "temperature": self.temperature_unit,
                    "humidity": self.humidity_unit,
                    "apparent_temp": self.apparent_temp_unit,
                    "precipitation": self.precipitation_unit,
                    "wind_speed": self.windspeed_unit,
                },
            }
        }

        if model not in db_data:
            db_data.append(model)
            with open(db_file, "w") as file:
                file.write(dumps(db_data))


current_weather = Weather(CITY)
print(current_weather)
current_weather.register_data(DB_FILE)
