import googlemaps
from decouple import config


def calculate_delivery_time(destination_location, cafe_location="41.2995,69.2401"):
    gmaps = googlemaps.Client(key=config('GOOGLE_KEY'))
    directions_result = gmaps.directions(cafe_location, destination_location, mode="walking")
    if directions_result:
        route = directions_result[0]['legs'][0]
        duration_in_traffic = route['duration']['value']
        return duration_in_traffic
    else:
        return None
