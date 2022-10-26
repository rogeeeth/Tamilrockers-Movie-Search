#Importing Module
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
  
#Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
  
#Input as a geek
loc = input("Enter the location: ")
print("Location address: ", loc)
  
#Getting Latitude and Longitud
location = geolocator.geocode(loc)
  
print("Latitude and Longitude of the said address:")
print((location.latitude, location.longitude))
  
#Pass the Latitude and Longitud
#Into a timezone_at
#and it return timezone
obj = TimezoneFinder()
  
#Returns 'Europe/Berlin'
res = obj.timezone_at(lng=location.longitude, lat=location.latitude)
print("Time Zone : ", res)
