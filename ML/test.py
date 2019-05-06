import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import svm
from IPython.display import SVG
#import from 

train_data = pd.read_csv('Kuzhi_labled.csv',usecols=['Gx','Gy','Gz'])
#train_data= np.array(train_data)
y = pd.read_csv('Kuzhi_labled.csv',usecols=['Class'])
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(train_data, y,test_size=.33, random_state=42)

from sklearn import tree
dtree = tree.DecisionTreeClassifier(max_depth=3)
dtree.fit(train_data, y)

from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus


import graphviz 
dot_data = tree.export_graphviz(dtree, out_file=None, 
                     feature_names=['Gx','Gy','Gz'],  
                     class_names=['0','1'],  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("a.pdf",view = True)
display(SVG(graph.pipe(format='svg')))