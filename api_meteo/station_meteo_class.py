import requests
from yaml import safe_load
from argparse import ArgumentParser

# Utilisation d'un fichier "secret" pour passer des variables à ne pas retrouver dans le code
with open("secret.yaml") as file:
    SECRETS = safe_load(file)

# Utilisation d'arguments pour passer des variables (ici le choix de la ville)
# Créer le parser
parser = ArgumentParser()
# Ajouter un argument
parser.add_argument("--ville", type=str, required=False)
# Passé l'argument
args = parser.parse_args()


class Meteo:
    def __init__(self, ville: str):
        self.ville = ville

    def get_meteo(self):
        # Requête pour récupérer lat et lon
        GEOLOC_API_KEY = SECRETS["api_key"]
        GEOLOC_URL = "http://api.openweathermap.org/geo/1.0/direct"
        GEOLOC_PARAMS = {"q": self.ville, "appid": GEOLOC_API_KEY}
        geoloc_req = requests.get(GEOLOC_URL, params=GEOLOC_PARAMS)
        geoloc_dict = geoloc_req.json()
        # Variable contenant l'ensemble de clé valeur

        dictionnaire_data = geoloc_dict[0]
        lat = dictionnaire_data["lat"]
        lon = dictionnaire_data["lon"]
        # lat et lon récupérés !

        # Requête pour récupérer données météorologiques
        WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
        WEATHER_PARAMS = {
            "latitude": lat,
            "longitude": lon,
            "current": [
                "temperature_2m",
                "relativehumidity_2m",
                "apparent_temperature",
                "precipitation",
                "windspeed_10m",
            ],
        }
        meteo_req = requests.get(WEATHER_URL, params=WEATHER_PARAMS)
        meteo_dict = meteo_req.json()
        # Tri du dictionnaire par les clés
        # lambda permet d'écrire une fonction sur une ligne et de récupérer un paramètre en direct
        current: dict = dict(sorted(meteo_dict["current"].items(), key=lambda t: t[0]))
        units: dict = dict(
            sorted(meteo_dict["current_units"].items(), key=lambda t: t[0])
        )
        print(f"Météo pour la ville de {self.ville} :")
        # zip() permet d'ittérer à travers plusieurs listes simultanément
        for definition, valeur, unit in zip(
            current.keys(), current.values(), units.values()
        ):
            # for (definition, valeur), unit in zip(current.items(), units.values()):
            print(f"{definition} : {valeur}{unit}")
        # Autre façon de faire pour deux dictionnaires avec clés similaires
        """ for key, value in current.items():
            print(f"{key} : {value}{units[key]}") """


if args.ville == None:
    meteo_actuelle = Meteo("strasbourg")
else:
    meteo_actuelle = Meteo(args.ville)
meteo_actuelle.get_meteo()
