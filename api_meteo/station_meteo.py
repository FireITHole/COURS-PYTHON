# REST : Representational State Transfer
# Une API est dite “Restful” lorsqu’elle respecte l’architecture REST, c’est-à-dire un ensemble de normes qui régissent la manière dont communique une application avec son environnement, que ce soit un outil tiers ou un autre composant de l'application.
# CRUD = Create, Read, Update, Delete
# Query parameter : directement dans l'url -> après le signe '?' premier parametre, nom du paramètre=valeur du paramètre, pour les prochain paramètres, séparation avec '&'
# URL Doc API Géolocalisation : https://openweathermap.org/api/geocoding-api
# URL Doc API météo : https://openweathermap.org/current

import requests
from datetime import datetime
from yaml import safe_load
import argparse


# Créer le parser
parser = argparse.ArgumentParser()
# Ajouter un argument
parser.add_argument("-k", type=str, required=False)
parser.add_argument("-c", type=str, required=False)
# Passé l'argument
args = parser.parse_args()


# Méthode permettant de récupérer la latitude et longitude d'une ville donnée et de récupérer ses infos météo
def get_weather(city: str) -> None:
    # On récupère la clé API dans un fichier contenant les "secrets"
    with open("secret.yaml") as file:
        SECRETS = safe_load(file)

    try:
        # On essaye de récupérer la clé api depuis le fichier "secret.yaml"
        GEOLOC_API_KEY = SECRETS["api_key"]
    except:
        # Sinon on essaye de le récupérer des arguements de commande
        GEOLOC_API_KEY = args.k

    # On défini l'url de la requête et ses paramètres pour une requête à l'API de conversion ville -> LAT, LON
    GEOLOC_URL = "http://api.openweathermap.org/geo/1.0/direct"
    GEOLOC_PARAMS = {"q": city, "appid": GEOLOC_API_KEY}

    # On fait la requête à l'API
    geoloc_res = requests.get(GEOLOC_URL, params=GEOLOC_PARAMS)
    geoloc_res = geoloc_res.json()

    # On extrait les données de la réponse API
    LAT = geoloc_res[0]["lat"]
    LON = geoloc_res[0]["lon"]

    # On défini l'url de la requête et ses paramètres pour une requête à l'API météo
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
    WEATHER_PARAMS = {
        "latitude": LAT,
        "longitude": LON,
        "current": [
            "temperature_2m",
            "relativehumidity_2m",
            "apparent_temperature",
            "precipitation",
            "windspeed_10m",
        ],
    }

    # On fait la requête à l'API
    weather_res = requests.get(WEATHER_URL, params=WEATHER_PARAMS)
    weather_res = weather_res.json()

    # On extrait ses données
    units: dict = weather_res["current_units"]
    current_vals: dict = weather_res["current"]

    # On print dans la console les résultat formatté
    print(
        f"Météo pour la ville de {city} à {datetime.now().strftime('%Hh%M')} :\n\
    - Température : {current_vals['temperature_2m']}{units['temperature_2m']}\n\
    - Humidité : {current_vals['relativehumidity_2m']}{units['relativehumidity_2m']}\n\
    - Température apparente : {current_vals['apparent_temperature']}{units['apparent_temperature']}\n\
    - Précipitation : {current_vals['precipitation']}{units['precipitation']}\n\
    - Vitesse du vent : {current_vals['windspeed_10m']}{units['windspeed_10m']}"
    )


# On récupère l'input de l'utilisateur pour choisir la ville si l'argument -c n'est pas fourni
if args.c != None:
    city = args.c
else:
    city = input("Choisissez une ville : ")

# On appelle la méthode pour récupérer les infos météo
get_weather(city)
