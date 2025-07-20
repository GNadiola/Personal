#Nadiola Grosvenor
#Recommendation System for Restaurants

#Imports
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import os

#Restaurant Storage
restaurants = pd.read_csv('restaurants.csv')

restaurants.head()