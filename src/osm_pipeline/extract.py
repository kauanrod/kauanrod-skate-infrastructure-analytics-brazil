import requests
import json

OVERPASS_URL = "http://overpass-api.de/api/interpreter"

query = """
[out:json][timeout:120];
area["name"="Brasil"]->.searchArea;
(
  node["leisure"="skateboard_park"](area.searchArea);
  way["sport"="skateboard"](area.searchArea);
  relation["sport"="skateboarding"](area.searchArea);
);
out center;
"""


def extract():
    response = requests.post(
        OVERPASS_URL, data={"data": query}, headers={"User-Agent": "Teste"}
    )

    response.raise_for_status()

    return response.json()


def save_raw(data):
    with open("data/raw/skateparks_raw.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
