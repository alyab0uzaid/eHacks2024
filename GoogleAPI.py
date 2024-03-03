#Get Location
from geopy.geocoders import Nominatim
import geocoder
import math
import googlemaps
 
def get_nearby_places(latitude, longitude, radius=15):
    api_key = "AIzaSyDgTK_zjQsy8tiTu_1WjycONJn1dEATTXA"
    gmaps = googlemaps.Client(key=api_key)

    # Make a request to the Places API using the 'places_nearby' method
    places_result = gmaps.places_nearby(location=(latitude, longitude), radius=radius)

    # Create an empty string to store the information
    result_string = ""

    # Extract information about places from the result
    for place in places_result['results']:
        place_name = place['name']
        #place_address = place['vicinity']
       # place_id = place['place_id']

        # Concatenate the information to the result_string
        result_string += f"Name: {place_name}\n"

    # Return the result_string
    return result_string