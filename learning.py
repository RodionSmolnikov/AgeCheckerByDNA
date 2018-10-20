# -*- coding: utf-8 -*-
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import tree
from sklearn import ensemble
from matplotlib import style
#%%
f = open("X_GSE36064.txt",'r')
s = f.read()
f.close()
s = s.split("\n")
s = s[:len(s)-1]
for i in range(len(s)):
    s[i]=s[i].split("\t")
for i in range(len(s)):
    s[i] = s[i][:len(s[i])-1]
    for j in range(len(s[0])):
        s[i][j]= float(s[i][j])
X_GSE36064 = s

f = open("X_GSE40279.txt",'r')
s = f.read()
f.close()
s = s.split("\n")
s = s[:len(s)-1]
for i in range(len(s)):
    s[i]=s[i].split("\t")

for i in range(len(s)):
    s[i] = s[i][:len(s[i])-1]
    for j in range(len(s[0])):
        s[i][j]= float(s[i][j])
X_GSE40279 = s
X_all = X_GSE40279 + X_GSE36064
X_all = np.array(X_all)

f = open("y_GSE36064.txt",'r')
s = f.read()
f.close()
s = s.split("\n")
s = s[:len(s)-1]
for i in range(len(s)):
    s[i] = int(float(s[i])*12)
y_GSE36064 = s

f = open("y_GSE40279.txt",'r')
s = f.read()
f.close()
s = s.split("\n")
s = s[:len(s)-1]
for i in range(len(s)):
    s[i] = int(float(s[i])*12)
y_GSE40279 = s
y_all = y_GSE40279 + y_GSE36064


X_test = X_all[:20]
y_test = y_all[:20]
X_all = X_all[20:]
y_all = y_all[20:]

#%%
"""дерево"""
print("tree")
clf_tree = tree.DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=10,
            max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False,
            random_state=1428298617, splitter='best')
start_dttm = time.clock()
clf_tree.fit(X_all,y_all)
finish_dttm = time.clock()
for i in range(len(X_test)):
    print(clf_tree.predict([X_test[i]])[0],y_test[i])
#%%
"""лес"""
print("forest")
clf_forest = ensemble.RandomForestClassifier(n_estimators=20, criterion="gini", max_depth=10, min_samples_split=2, min_samples_leaf=1)
start_dttm = time.clock()
clf_forest.fit(X_all,y_all)
finish_dttm = time.clock()
for i in range(len(X_test)):
    print(clf_forest.predict([X_test[i]])[0],y_test[i])
#%%
"""регрессия"""
print("regression")
clf = svm.SVR(kernel= 'linear', C = 1, degree = 3)
print("linear")
start_dttm = time.clock()
clf.fit(X_all,y_all)
print("fit_done")
finish_dttm = time.clock()
print("time is",finish_dttm - start_dttm)
for i in range(len(X_test)):
    print(clf.predict([X_test[i]])[0],y_test[i])
#%%
tree.export_graphviz(clf_tree,  out_file='tree.dot') 
plt.plot(clf_tree.feature_importances_)
plt.plot(clf_forest.feature_importances_)
