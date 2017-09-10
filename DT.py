import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

balance_data = pd.read_csv("dt-num-data.txt" ,sep= ', ', header= None, engine='python')
print "dataset length ", len(balance_data)
print "Dataset Shape:: ", balance_data.shape
#print "Dataset:: "
#balance_data.head()

#converting our dataframes into numpy arrays
X = balance_data.values[:, 0:6];
Y = balance_data.values[:, 6];

#Separate data to train and test set 
X_train, X_test, y_train, y_test = train_test_split( X, Y,test_size = 0.3)

#Information gain algo
clf_entropy = DecisionTreeClassifier(criterion = "entropy")
clf_entropy.fit(X_train, y_train)

DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=5,
            max_features=None, max_leaf_nodes=None, min_samples_leaf=5,
            min_samples_split=2, splitter='best')
y_pred_en = clf_entropy.predict(X_test)

with open("funnight_classifier.txt", "w") as f:
    f = tree.export_graphviz(clf_entropy, out_file=f)

