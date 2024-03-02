#Get Location
from geopy.geocoders import Nominatim
import geocoder
import math
import googlemaps
 
# calling the Nominatim tool
#loc = Nominatim(user_agent="my_app")
 
# entering the location name
#getLoc = loc.geocode("Southern Illinois University Edwardsville")
 
# printing address
#print(getLoc.address)
 
# printing latitude and longitude
#print("Latitude = ", getLoc.latitude, "\n")
#print("Longitude = ", getLoc.longitude)

g = geocoder.ip('me')
print(g.latlng)

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'AIzaSyDD-pZruqPkWXtxfWOb1JicAROzEyeP2C0'
gmaps = googlemaps.Client(key=api_key)

# Define the radius (in meters) around the location to search for places
radius = 30  # Replace with your desired radius
latitude = 38.7944294995016
longitude = -90.0005243251564
# Make a request to the Places API using the 'nearby_search' method
places_result = gmaps.places_nearby(location=(latitude, longitude), radius=radius)

# Extract information about places from the result
for place in places_result['results']:
    place_name = place['name']
    place_address = place['vicinity']
    place_id = place['place_id']

    print(f"Name: {place_name}\nAddress: {place_address}\nPlace ID: {place_id}\n---")


#User mode Keywords
study = {"Library", "University" }
chill = { }
gym = {"Fitness", "Gym", "Recreational"} 
