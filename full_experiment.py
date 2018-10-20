# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
#%%
"""работа с файлом данных и получение бета-значений"""
print("work with table")
f = open("GSE36064_non-normalized_easy.txt","r")
s = f.read()
f.close
s = s.split("\n")

for i in range(len(s)):
    s[i]=s[i].split("\t")

for i in range(1,len(s[0])):
    tmp = s[0][i].split(' ')
    if tmp[2]=='Pval':
        s[0][i] = tmp[0]

for j in range(1,len(s)):
    for i in range(1,len(s[j])):
        if s[j][i] == '0.00' and int(s[j][i-1])!=0 and int(s[j][i-2])!=0:
            s[j][i] = int(s[j][i-1])*1.0/(int(s[j][i-1])+int(s[j][i-2]))
        else:
            s[j][i]=float(s[j][i])

#%%
"""транспонирование"""
print("transpose")

#print(s[0][:4])
a = np.array(s)
print(len(s))
print(len(s[2]))
print(a.shape)
a = a.transpose()
#a = list(zip(*s))
#a = np.array(a)
print(a.shape)
#print(s[:2])
#%%
"""выделение полезной информации"""
print("usefull info")
data =[]
for i in a:
    if len(i[0].split(' '))==1 and i[0]!='NA':
        data.append(i)
#print(data[:10])

#%%
"""получение списка образцов"""
print("taking samples")
samples = []
for i in data:
    samples.append(i[0])
samples = samples[1:]
#print(samples)
#%%
print("urllib")
import urllib
url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE36064'
#url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM879996'
response = urllib.request.urlopen(url) 
html = response.read()
s = str(html)
samples_age = {}
for sample in samples:
    url_sample = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=' + s[s.find('Harvard Sib ' + sample)-37:s.find('Harvard Sib ' + sample)-37+9]
    print(url_sample)
    response = urllib.request.urlopen(url_sample) 
    html = response.read()
    subs = str(html)
    subs = subs.split('age at collection months: ')[1]
    subs = subs.split('<')[0]
    age = int(subs)*1.0/12
    samples_age.update({sample:age})
#%%
"""подготовка даты для регрессии"""
print("data for regression")
print(samples_age)
data = data[1:]
X = []
for i in range(len(data)):
    data[i]=data[i][1:]
    tmp = []
    for j in range(len(data[i])):
        tmp.append(float(data[i][j]))
    X.append(tmp)
y = []
for i in samples_age:
    y.append(samples_age[i])
#%%
"""регрессия"""
print("regression")


from sklearn import svm
from sklearn import tree
import time

clf_tree = tree.DecisionTreeRegressor(max_depth = 5, min_samples_split = 3, min_samples_leaf = 0.3,
                                       random_state = 17)
clf = svm.SVR(kernel= 'linear', C = 1, degree = 3)
print("here")
start_dttm = time.clock()
clf.fit(X[:len(X)-1],y[:len(X)-1])
print("fit_done")
finish_dttm = time.clock()
print(finish_dttm - start_dttm)
#%%
"""предсказание"""
print("prediction")
print(str(clf.predict([X[-1]])))
print(y[-1])







