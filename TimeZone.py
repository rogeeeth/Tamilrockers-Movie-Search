# importing module
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
  
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
  
# input as a geek
lad = input("Enter the location: ")
print("Location address:", lad)
  
# getting Latitude and Longitud
location = geolocator.geocode(lad)
  
print("Latitude and Longitude of the said address:")
print((location.latitude, location.longitude))
  
# pass the Latitude and Longitud
# into a timezone_at
# and it return timezone
obj = TimezoneFinder()
  
# returns 'Europe/Berlin'
result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
print("Time Zone : ", result)
