#Nadiola Grosvenor
#Recommendation System for Restaurants

#Imports
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import os


# creating a new column for cuisine types
from yelpapi import YelpAPI

#Restaurant Storage
raw_url = 'https://raw.githubusercontent.com/GNadiola/Personal/96fd8e9f91817b9fc9fffd9f225646d22de71863/Raleigh%20Food%20Recommendation%20System/restaurants.csv'
restaurants = pd.read_csv(raw_url)


# Load Wake County locations
restaurants = pd.read_csv(raw_url)


#Testing
restaurants = restaurants.sample(10, random_state=42).copy()


#Getting the cuisine column from Yelp
api_key = 'XEAINaSFMQU2Bx4yVVhvPO1kApQzf9vPps7gBQMztPcCyqdgt2G0FXMpl5A_L0pgsVGyNf9FfwHy-Fj79lXujjY9oZdtoElnsbtuUOaY5HLRmqTAFMF1zkkoyE9-aHYx'
yelp_key = YelpAPI(api_key)


def get_cuisine(name, address):
    try:
        res = yelp_key.search_query(term=name, location=address, limit=1)
        if len(res['businesses']) == 0:
            return ['No Results']
        categories = res['businesses'][0]['categories']
        return [cat['title'] for cat in categories] if categories else ['No Category']
    except Exception as e:
        print(f"Error for {name} at {address}: {e}")
        return ['Error']

restaurants['CUISINE'] = restaurants.apply(
    lambda r: get_cuisine(r['NAME'].split('#')[0].split('(')[0].strip(),
    f"{r['ADDRESS1']}, {r['CITY'].replace('-', ' ').title()}"
    ), axis=1
)


#The data I want to keep
#cities, address1, address2, name, state, postalcode, phonenumber
restaurants = restaurants[['NAME','PHONENUMBER','ADDRESS1','ADDRESS2','CITY','STATE','POSTALCODE','CUISINE']]

print(restaurants.head(1))