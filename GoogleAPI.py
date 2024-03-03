
import googlemaps
import math

places_info_list = []


def get_nearby_places_with_distance(latitude, longitude, radius=15):
    api_key = "AIzaSyDgTK_zjQsy8tiTu_1WjycONJn1dEATTXA"
    gmaps = googlemaps.Client(key=api_key)

    places_result = gmaps.places_nearby(location=(latitude, longitude), radius=radius)

    places_info_list = []

    for place in places_result['results']:
        place_name = place['name']
        place_address = place['vicinity']
        place_location = place['geometry']['location']
        place_latitude = place_location['lat']
        place_longitude = place_location['lng']

        distance = haversine(float(latitude), float(longitude), float(place_latitude), float(place_longitude))

        if distance <= 30:
            place_info = {
                'name': place_name,
                'address': place_address,
                'coordinates': (place_latitude, place_longitude),
                'distance': distance
            }
            places_info_list.append(place_info)

    return places_info_list

def haversine(lat1, lon1, lat2, lon2):
    #print(f"lat1: {lat1}, lon1: {lon1}, lat2: {lat2}, lon2: {lon2}")
    R = 6371000  # Earth radius in meters
    dlat = math.radians(float(lat2) - float(lat1))
    dlon = math.radians(float(lon2) - float(lon1))
    a = math.sin(float(dlat) / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return float(distance)