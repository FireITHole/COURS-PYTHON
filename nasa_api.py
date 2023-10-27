import requests
from json import loads, dumps
from datetime import datetime, timedelta

API_KEY = "DP9VWlPfn0zcnOjjTq7AlGsL06K0hIsNROGmEZ7b"
END_DATE = (datetime.now() + timedelta(days=0)).strftime("%Y-%m-%d")
NASA_ENDPOINT = f"https://api.nasa.gov/neo/rest/v1/feed?end_date={END_DATE}&api_key={API_KEY}"

req = requests.get(NASA_ENDPOINT)
REQ_JSON = req.json()

with open("neo.json", "w") as file:
    file.write(dumps(REQ_JSON))

""" with open("neo.json") as file:
    content = loads(file.read())
    print(content) """