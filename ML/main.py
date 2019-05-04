import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import time
import json
#import from another python file 
import convert_togeojson as call 

start = time.time()

#filename of the csv file
file_name='Kuzhi' 
train_data = pd.read_csv(file_name+'.csv',usecols=['Gx','Gy','Gz'])
train_data= np.array(train_data)
print(train_data)

import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["local"]
mycol = mydb["data"]
#mydict = {"lat": "10.1212","lon":"125223"}
#x = mycol.insert_one(mydict)

data_json = json.loads(train_data.to_json(orient='records'))
mycol.insert(data_json)

#clystering the data with center 100 points and distance .8
clustering = DBSCAN(eps=.8, min_samples=100).fit(train_data)
print("Clustering completed")

labels = np.asarray(clustering.labels_)

#reading the complete file for adding the label
com_data = pd.read_csv(file_name+'.csv')

df2 = pd.DataFrame(labels)
df1=pd.DataFrame(com_data)
df1['Class']=df2
print(df1)
df1.to_csv(file_name+"_labled.csv", sep=",", encoding='utf-8',index=False)

#printing the time requires to execute 
end = time.time()
print(end - start)

print("pothole count")
print(df1['Class'].value_counts())

#filter pothole

pothole_data=df1.loc[df1['Class'] == -1]
print(pothole_data)


#pothole only data
df_pothole = pothole_data[['Lat','Lon','Class']]
df_pothole.to_csv(file_name+"_pothole.csv", sep=",", encoding='utf-8',index=False)
print(df_pothole)

df_pothole.to_json('temp.json', orient='records', lines=True)

#creating a geojson file for mapping purpose
cols=['Lat','Lon']
pot=pd.read_csv(file_name+"_pothole.csv")
plot = call.df_to_geojson(pot,cols)
with open('pothole_coordinates.geojson','w') as out:
    json.dump(plot,out)
    
#plotting the value in 3d 
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#x = np.array(df1['Gx'])
#y = np.array(df1['Gy'])
#z = np.array(df1['Gz'])
#ax.scatter(x,y,z, marker="s", c=clustering.labels_)
#plt.show()