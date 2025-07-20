#Nadiola Grosvenor
#Recommendation System for Restaurants

#Imports
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import os

#Restaurant Storage
raw_url = 'https://raw.githubusercontent.com/GNadiola/Personal/96fd8e9f91817b9fc9fffd9f225646d22de71863/Raleigh%20Food%20Recommendation%20System/restaurants.csv'
restaurants = pd.read_csv(raw_url)

restaurants.head(1)

#Sorting the cities
restaurants['CITY'].value_counts()