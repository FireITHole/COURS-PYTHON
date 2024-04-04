import sqlite3
import requests
from yaml import safe_load, YAMLError
from datetime import datetime

with open("secrets.yaml") as file:
    try:
        SECRETS: dict = safe_load(file)
    except YAMLError as err:
        print(err)
        exit(1)

# """CREATE TABLE MeteoData (
#       id INTEGER PRIMARY KEY,
#       timestamp DATETIME NOT NULL,
#       city TEXT NOT NULL, 
#       temperature REAL,
#       humidity REAL,
#       wind_speed REAL,
#       pressure REAL
#    );
# """

def print_weather_data() -> None:
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM MeteoData")
        print(cur.fetchall())

def store_weather_data(weather_data: dict) -> None:    
    with sqlite3.connect("test.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO MeteoData (timestamp, city, temperature, humidity, wind_speed, pressure) VALUES (?, ?, ?, ?, ?, ?)", tuple(weather_data.values()))
        con.commit()

def get_weather_data(city: str) -> dict:
        geoloc_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={SECRETS['api_key']}"
        geoloc_res = requests.get(geoloc_url)
        geoloc_res = geoloc_res.json()

        lat = geoloc_res[0]["lat"]
        lon = geoloc_res[0]["lon"]

        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={SECRETS['api_key']}&units=metric&lang=fr"
        weather_res = requests.get(weather_url)
        weather_res = weather_res.json()

        return {"timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "city": weather_res['name'], "temperature": weather_res['main']['temp'], "humidity": weather_res['main']['humidity'], "wind_speed": weather_res['wind']['speed'], "pressure": weather_res['main']['pressure']}


weather_data = get_weather_data("strasbourg")
print(weather_data)
store_weather_data(weather_data)
print_weather_data()








