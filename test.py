import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import time

start = time.time()

#filename of the csv file
file_name='kaiparambu_nice_labled' 
train_data = pd.read_csv(file_name+'.csv',usecols=['Lat','Lon','Class'])

df = pd.DataFrame(train_data)
val=df.loc[df['Class'] == -1]

print(val)