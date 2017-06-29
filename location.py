from geopy.geocoders import Nominatim
from geopy.distance import vincenty

geolocator = Nominatim()
location = geolocator.geocode("goa")
gloc1 = (location.latitude, location.longitude)

location2 = geolocator.geocode("hyderabad")
gloc2 = (location2.latitude, location2.longitude)
print(vincenty(gloc1, gloc2).miles)
