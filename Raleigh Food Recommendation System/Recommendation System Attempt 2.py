#Nadiola Grosvenor
#Food Recommendation System Attempt 2

#import my other code with the restaurants data
from Data_Loader_Code import dlc


#Opening message
print("Welcome to the Raleigh Restaurant Reach!")
print("Looking for a place to eat? You've come to the right place!")
print("Let's get started!!")

#Select search or recommendation
print("Are you looking for a specific place to eat or searching for recommendations?")
#Click button to pick which option in html


#For a specific place to eat
#Search bar
search = str(input("Where would you like to eat?\nSearch by name or location.")).lower()
matching_words = []

result = dlc(get_cuisine))
business = result['businesses'][0]
    
if result:
    print("\n✅ Restaurant Found:")
    print("Name:", business['name'])
    print("Address:", ", ".join(business['location']['display_address']))
    print("Rating:", business['rating'])
    print("Cuisine:", ", ".join([cat['title'] for cat in business['categories']]))
    print("Phone:", business['phone'])
else:
    print("\n❌ No results found.")
