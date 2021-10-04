from folium import Map

latitude = float("140.09")
longitude = float("63.47")

antipode_latitude = latitude.__mul__(int("-1"))

if longitude.__lt__(float("0")):
    antipode_longitude =  longitude.__add__(float("180"))
elif longitude.__eq__(float("0")):
    antipode_longitude = float("180")
elif longitude.__gt__(float("180")):
        antipode_longitude = str("Invalid longitude")
        
else:
    antipode_longitude =  longitude.__sub__(float("180"))
location =list ((antipode_latitude, antipode_longitude))
mymap =Map(location)    
mymap.save(str("antipode.html"))

print(antipode_latitude)
print(antipode_longitude)
print(mymap)
