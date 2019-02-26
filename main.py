import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import time

start = time.time()

#filename of the csv file
file_name='kaiparambu_nice' 
train_data = pd.read_csv(file_name+'.csv',usecols=['Gx','Gy','Gz'])
train_data= np.array(train_data)
print(train_data)

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
df1.to_csv(file_name+"_labled.csv", sep=",", encoding='utf-8')

#printing the time requires to execute 
end = time.time()
print(end - start)

#plotting the value in 3d 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.array(train_data['Gx'])
y = np.array(train_data['Gy'])
z = np.array(train_data['Gz'])
ax.scatter(x,y,z, marker="s", c=clustering.labels_)
plt.show()
