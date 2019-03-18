
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import svm
#import from 

train_data = pd.read_csv('Kuzhi_labled.csv',usecols=['Gx','Gy','Gz'])
train_data= np.array(train_data)
y = pd.read_csv('Kuzhi_labled.csv',usecols=['Class'])

clf = svm.SVC(gamma='scale')
clf = clf.fit(train_data, y)

test_x = pd.read_csv('kaiparambu_nice_labled.csv',usecols=['Gx','Gy','Gz'])
test_x= np.array(test_x)
test_y = pd.read_csv('kaiparambu_nice_labled.csv',usecols=['Class'])
pre=clf.predict(test_x)
df = pd.DataFrame({'col':pre})
print(df['col'].value_counts())
print(clf.score(test_x,test_y))