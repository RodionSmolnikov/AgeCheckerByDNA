# -*- coding: utf-8 -*-
"""GSE40279"""

"""работа с файлом данных и получение бета-значений"""
print("work with table")
f = open("GSE40279_average_beta_GSM989827-GSM989990_easy.txt","r")
s = f.read()
f.close
s = s.split("\n")

for i in range(len(s)):
    s[i]=s[i].split("\t")
for i in range(len(s)):
    for j in range(1,len(s[0])):
        s[i][j]= float(s[i][j])

#%%
"""выбор общих CG"""
f = open("CG.txt",'r')
CG = f.read()
f.close()
CG = CG.split('\n')
data = []
for i in s:
    exception = 0
    try:
        CG.index(i[0])
    except ValueError:
        exception = 1
    if exception == 0:
        data.append(i)
s = data
#%%
import numpy as np
a = np.array(s)
for i in range(len(a)):
    a[i] = np.array(a[i])
a = a.transpose()
a = a[1:]
print(len(a[0]))
#%%

f = open("GSE40279_age.txt",'r')
s = f.read()
f.close()
s = s.split('\n')
for i in range(len(s)):
    s[i]=s[i].split("\t")
    s[i]=s[i][1]
for i in range(len(s)):
    s[i]=s[i].split(' ')
    s[i]=s[i][1][:len(s[i][1])-1]
    s[i]=int(s[i])
y = s

#%%
"""запись в файлы"""
f = open("X_GSE40279.txt",'w')
for i in a:
    for j in i:
        f.write(str(j))
        f.write('\t')
    f.write('\n')
f.close()

f = open("y_GSE40279.txt",'w')
for i in y:
    f.write(str(i))
    f.write('\n')
f.close()
