import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#docstring
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def colour_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nam in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nam, nam, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), fill_color=colour_producer(el), color='grey', fill_opacity=0.7))

map.add_child(fg)
map.save("Map1.html")