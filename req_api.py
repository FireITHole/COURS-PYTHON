# REST : Representational State Transfer
# Une API est dite “Restful” lorsqu’elle respecte l’architecture REST, c’est-à-dire un ensemble de normes qui régissent la manière dont communique une application avec son environnement, que ce soit un outil tiers ou un autre composant de l'application.
# CRUD = Create, Read, Update, Delete

import requests
from json import loads, dumps

""" URL = "https://creativness-records.com/api"

res = requests.get(URL)
print(res)
res = res.status_code
print(res) """

###

# Query parameter : directement dans l'url -> après le signe '?' premier parametre, nom du paramètre=valeur du paramètre, pour les prochain paramètres, séparation avec '&'

WEATHER_URL = "https://api.open-meteo.com/v1/forecast?latitude=48.5839&longitude=7.7455&current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,windspeed_10m"
weather_res = requests.get(WEATHER_URL)
weather_res = weather_res.json()
# print(weather_res)

""" with open("meteo.json", "w") as file:
    file.write(dumps(weather_res)) """

units: dict = weather_res['current_units']
current_vals: dict = weather_res['current']

for key, val in current_vals.items():
    print(f"{key} : {val}({units[key]})")

###

#print(requests.post("http://localhost:3001/api", json={"message": "test"}).json())