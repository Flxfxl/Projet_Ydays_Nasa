import requests
import pandas as pd
from datetime import datetime, timedelta

api_key = "C8FWmOXnfReN5yJb1vb0yay0JwtgHTFyEDulhN9Z"
start_date = datetime(2025, 1, 1)
end_date = datetime.today()

all_objects = []

# L'API feed n'autorise que 7 jours max par requête
delta = timedelta(days=7)
current_start = start_date

while current_start <= end_date:
    current_end = min(current_start + delta, end_date)
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "start_date": current_start.strftime("%Y-%m-%d"),
        "end_date": current_end.strftime("%Y-%m-%d"),
        "api_key": api_key
    }
    print(f"Récupération {current_start.date()} → {current_end.date()}")
    resp = requests.get(url, params=params)
    data = resp.json()

    # Chaque jour a sa propre liste de NEO
    for day in data["near_earth_objects"]:
        all_objects.extend(data["near_earth_objects"][day])

    current_start = current_end + timedelta(days=1)

print(f"Total objets récupérés depuis 2025 : {len(all_objects)}")

# Convertir en DataFrame
df = pd.json_normalize(all_objects)
df.to_csv("neo_2025_to_now.csv", index=False)
print("CSV sauvegardé : neo_2025_to_now.csv")
