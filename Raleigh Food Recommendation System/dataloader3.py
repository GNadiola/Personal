import requests
import pandas as pd

API_KEY = 'XEAINaSFMQU2Bx4yVVhvPO1kApQzf9vPps7gBQMztPcCyqdgt2G0FXMpl5A_L0pgsVGyNf9FfwHy-Fj79lXujjY9oZdtoElnsbtuUOaY5HLRmqTAFMF1zkkoyE9-aHYx'
HEADERS = {'Authorization': f'Bearer {API_KEY}'}

def get_business_info(name, location):
    url = "https://api.yelp.com/v3/businesses/search"
    params = {
        "term": name,
        "location": location,
        "limit": 1
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["businesses"]:
            return data["businesses"][0]  # Most relevant match
    return None


df = pd.read_csv("Restaurants_in_Wake_County.csv")

def enrich_with_cuisine(row):
    info = get_business_info(row['NAME'], row['CITY'] + ", " + row['STATE'])
    if info:
        return ', '.join([cat['title'] for cat in info['categories']])
    return None

df['cuisine'] = df.apply(enrich_with_cuisine, axis=1)
df.to_csv("enriched_restaurants.csv", index=False)
