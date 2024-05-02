import geopy.distance


def calculate_distance(destination_location, cafe_location=(41.341524, 69.337170)):
    print(geopy.distance.distance(destination_location, cafe_location).km)
    return geopy.distance.geodesic(destination_location, cafe_location).km
