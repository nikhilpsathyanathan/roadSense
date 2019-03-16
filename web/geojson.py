import pandas as pd
import json
x = pd.read_csv("pothole.csv")

def df_to_geojson(df, properties, lat='Lat', lon='Lon'):
    geojson = {'type':'FeatureCollection', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature','properties':{},'geometry':{'type':'Point','coordinates':[]}}
        feature['geometry']['coordinates'] = [row[lon],row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson


cols=['Lat','Lon']
geojson=df_to_geojson(x,cols)

with open('web.geojson','w') as outfile:
    json.dump(geojson,outfile)
print(geojson)