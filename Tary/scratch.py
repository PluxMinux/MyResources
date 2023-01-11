import phonenumbers
from phonenumbers import geocoder



number = "+639562918092"

#Country Location of Phone number
sanNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber, "en")
print(yourLocation)


#ISP of the number
from phonenumbers import carrier

ISP = phonenumbers.parse(number)
print(carrier.name_for_number(ISP, "en"))



#Display in the Map the location of Phone Number
from opencage.geocoder import OpenCageGeocode
token = "26307444f8944dbaad787a1aa24e9f2a"

geocoder = OpenCageGeocode(token)

query = str(yourLocation)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

import folium
onMap = folium.Map(location=[lat,lng], zoom_start = 9)
folium.Marker([lat,lng], popup=yourLocation).add_to((onMap))

onMap.save("mapLocation.html")