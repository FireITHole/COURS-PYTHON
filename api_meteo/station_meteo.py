# REST : Representational State Transfer
# Une API est dite “Restful” lorsqu’elle respecte l’architecture REST, c’est-à-dire un ensemble de normes qui régissent la manière dont communique une application avec son environnement, que ce soit un outil tiers ou un autre composant de l'application.
# CRUD = Create, Read, Update, Delete

import requests
from datetime import datetime
from yaml import safe_load

# Query parameter : directement dans l'url -> après le signe '?' premier parametre, nom du paramètre=valeur du paramètre, pour les prochain paramètres, séparation avec '&'

# URL Doc API Géolocalisation : https://openweathermap.org/api/geocoding-api#direct

with open("secret.yaml") as file:
    SECRETS = safe_load(file)

GEOLOC_API_KEY = SECRETS["api_key"]

try:
    CITY = SECRETS["ville"]
except:
    CITY = input("Choisissez la ville pour votre station météo : ")

GEOLOC_URL = (
    f"http://api.openweathermap.org/geo/1.0/direct?q={CITY}&appid={GEOLOC_API_KEY}"
)
geoloc_res = requests.get(GEOLOC_URL)
geoloc_res = geoloc_res.json()

LAT = geoloc_res[0]["lat"]
LON = geoloc_res[0]["lon"]

WEATHER_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,windspeed_10m"
weather_res = requests.get(WEATHER_URL)
weather_res = weather_res.json()

units: dict = weather_res["current_units"]
current_vals: dict = weather_res["current"]

print(
    f"Météo pour la ville de {CITY} à {datetime.now().strftime('%Hh%M')} :\n\
    - Température : {current_vals['temperature_2m']}{units['temperature_2m']}\n\
    - Humidité : {current_vals['relativehumidity_2m']}{units['relativehumidity_2m']}\n\
    - Température apparente : {current_vals['apparent_temperature']}{units['apparent_temperature']}\n\
    - Précipitation : {current_vals['precipitation']}{units['precipitation']}\n\
    - Vitesse du vent : {current_vals['windspeed_10m']}{units['windspeed_10m']}"
)
