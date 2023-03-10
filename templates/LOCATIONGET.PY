from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-app-name") # Replace "my-app-name" with your own user agent

latitude = 13.055621643460691
longitude = 80.14803417560618

location = geolocator.reverse(f"{latitude}, {longitude}", zoom=18)
print(location.address)
