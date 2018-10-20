# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:54:28 2018

@author: s.bazhenov
"""
"""обработка таблицы"""

f = open("таблица экспериментов.txt",'r')
s = f.read()
f.close

s = s.split("\n")

for i in range(len(s)):
    s[i] = s[i].split(",")
info = [0]*len(s)
for i in range(len(s)):
    info[i]=[0]*4
    info[i][0] = s[i][2]
    info[i][1] = s[i][7]
    info[i][2] = s[i][5][2:4]
    info[i][3] = s[i][8]
info = info[1:]


#%%
f = open("таблица экспериментов удобная.txt",'w')
for i in info:
    if i[0]=='450K' and i[3].find("GSE")>=0: 
        #f.write(i[0]+" "+i[3]+" "+i[2]+'\n')
        f.write(i[3]+'\n')
f.close()

#%%
"""https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc="""
"""https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE41037&format=file&file=GSE41037%5FMatrix%5Fsignal%5Fintensities%2Etxt%2Egz"""
"""https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE41037&format=file&file=GSE41037%5Fnon%5Fnormalized%2Etxt%2Egz"""
"""https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE38873&format=file&file=GSE38873%5Fmatrix%5Fsignal%2Etxt%2Egz"""
"""скачивание информации"""
import urllib

f = open("таблица экспериментов удобная.txt",'r')
main_s = f.read()
f.close
main_s = main_s.split("\n")
for MAIN_I in main_s:
    print(MAIN_I)
    if MAIN_I!='':
        main_url = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='+MAIN_I
    print(main_url)
    
    response = urllib.request.urlopen(main_url) 
    html = response.read()
    #print(html)
    s = str(html)
    a = s.index("Supplementary file")
    if s.find("Supplementary data files not provided")==-1:
        if s.find("Raw data is available on Series record")==-1:
            b = s.index("Raw data not provided for this record")
        else:
            b = s.index("Raw data is available on Series record")
    else:
        continue;
    print(a)
    s = s[a:b]
    s = s.split("href=")
    tmp = []
    for i in range(len(s)):
        if s[i].find("/geo")==1:
            tmp.append(s[i])
    s = tmp
    for i in range(len(s)):
        s[i]=s[i].split(";")
#    for i in s:
#        print(i)
    count = 0
    for i in s:
        url = 'https://www.ncbi.nlm.nih.gov'
        count = count+1
        for j in range(len(i)):
            if j==0:
                url = url + i[j][1:28]
            if j==1:
                url = url + "&" + i[j][:11]
            if j==2:
                tmp = i[j].find(">(")
                url = url + "&" + i[j][:tmp-1]
            #тут скачивание
            """
            urllib.urlretrieve(url, MAIN_I+".txt.gz")
            print(url)
            print(MAIN_I+".txt.gz")
            """
        print(url)
        file_from_url = urllib.request.urlopen(url).read()
        f = open(MAIN_I+"_"+str(count)+".txt.gz", "wb")
        f.write(file_from_url)
        f.close()
            
            