# -*- coding: utf-8 -*-
"""
Creating a decision tree using numeric and categorical data

@author: SkYe
"""

import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_curve,auc
from statsmodels.tools import categorical
from sklearn.model_selection import train_test_split


data = pd.read_csv("C:/Users/SkYe/Documents/Python_Scripts/data/adult.csv", 
                     header = 0)
data.columns

len(data)
# 32561
len(data)*0.8
len(data)*0.2

#alternative
#rand_sel = np.random.rand(len(data)) < 0.8
#train = data[rand_sel]
#test = data[~rand_sel]

# Convert categorical target
data[' class'].values
data[' classnum'] = data[' class'].map({' moreThan50K': 1, ' lessThan50K': 0})
data = data.drop(' class', 1)


train, test = train_test_split(data, 
                               test_size = 0.2) #80/20 SPLIT

                        
                               
cols_to_transform = [ ' workclass', 
                    ' education', 
                    ' marital-status', 
                    ' occupation', 
                    ' relationship', 
                    ' race',
                    ' sex',
                    ' native-country']

                    
train_data_with_dms = pd.get_dummies(train, 
                                   columns = cols_to_transform )
test_data_with_dms = pd.get_dummies(test, 
                                   columns = cols_to_transform )



print test_data_with_dms.columns

list(set(train_data_with_dms.columns) - set(test_data_with_dms.columns))

test_data_with_dms[' occupation_ Armed-Forces'] = 0


test_outcome = test_data_with_dms[' classnum']

test_data_with_dms = test_data_with_dms.drop(' classnum', 1)


y = targets = labels = train_data_with_dms[' classnum'].values

columns = list(train_data_with_dms.columns.values)
features = train_data_with_dms[list(columns)].values
X = features


#from sklearn.preprocessing import Imputer
#imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
#X = imp.fit_transform(features)
#X

from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X, y)

clf

from sklearn.externals.six import StringIO
with open("data/adult.dot", 'w') as f:
  f = tree.export_graphviz(clf, out_file=f, feature_names=columns)


#import pydotplus 
#dot_data = tree.export_graphviz(clf, out_file=None) 
#graph = pydotplus.graph_from_dot_data(dot_data) 
#graph.write_pdf("data/adult.pdf") 
