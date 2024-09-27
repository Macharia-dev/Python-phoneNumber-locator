import phonenumbers
import opencage
from myphone import number
import folium

from phonenumbers import geocoder

pepnumber = geocoder.parse(number)
location = geocoder.description_for_number(pepnumber,"en")

print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode

key = '2460e7279edb4c238dbf0772d97d3443'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print (results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

mymap = folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng], popup=location).add_to(mymap)

mymap.save("mylocation.html")

