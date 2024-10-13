import geopy

def geolocate(city):
    """Get the latitude and longitude of a specific location."""
    
    full_name, coordinates = geocoder.geocode(city)
    return coordinates

# Select geocoding service provided by OpenStreetMap's Nominatim - https://wiki.openstreetmap.org/wiki/Nominatim
geocoder = geopy.geocoders.Nominatim(user_agent="comp0233") 

geolocate(city='Cambridge')