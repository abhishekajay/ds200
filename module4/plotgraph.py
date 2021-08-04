import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from statistics import median
from matplotlib.ticker import MultipleLocator
filehandle=open("Table_2018_6.4.csv","r")
year=[]
var=[]
flag=0
count=1
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() ) #different object reference each time
    return list_of_objects
for l in filehandle:
    var=len(l.split(","))-1
    year=l.split(",")[1:]
    break
var=int(var)
data = init_list_of_objects(var)
data1 = init_list_of_objects(var)
for line in filehandle:
    a=line.split(",")
    if count==1: 
        count=count+1
    if a[0][0]=="T":
        flag=1
    if (count >1 and a[0][0]!="T" and a[0][0]!="N" and flag==0 ):
        data[0].append(float(a[1]))
        data[1].append(float(a[2]))
        data[2].append(float(a[3]))
        data[3].append(float(a[4]))
        data[4].append(float(a[5]))
        data[5].append(float(a[6]))
        data[6].append(float(a[7]))
        count=count+1
    elif (a[0][0]!="T" and a[0][0]!="N" and flag==1):
        data1[0].append(float(a[1]))
        data1[1].append(float(a[2]))
        data1[2].append(float((a[3])))
        data1[3].append(float(a[4]))
        data1[4].append(float(a[5]))
        data1[5].append(float(a[6]))
        data1[6].append(float(a[7]))
        count=count+1

# the first scatter plot aims to compare the import and 
# export values of petroleum products between 2011-2018
#for i in range(12):
#    print(len(data[0]),len(year))
#    sys.exit()
pltdata=init_list_of_objects(len(data1[0]))
markersym=['o','^','+','x']
for p in range(6):
    for q in range(var):
        pltdata[p].append(data1[q][p])
legends=["LPG","Petrol","Naphtha","ATF","Kerosene","Diesel"]
#scatter plot is figure(1)
plt.figure(1)
for i in range(6):
    plt.scatter(year,pltdata[i],marker=markersym[i%4],label=legends[i])
plt.title('Plot of Export quantity of Petroleum products at different year spans',color='blue',fontsize=20)
plt.xlabel('Year',fontsize=15,color='blue')
plt.ylabel('Export Quantity',fontsize=15,color='blue')
plt.legend(loc='upper left')
plt.grid(linestyle='dotted')
#bar plot is figure(2)
plt.figure(2)
plt.xlabel('Petroleum Products',color='blue',fontsize=15)
plt.ylabel('Export Quantity',color='blue',fontsize=15)
plt.title('Box plot showing Petroleum products on x axis and Export quantity on y axis',color='blue',fontsize=20)
plt.boxplot(pltdata,labels=['LPG','Petrol','Naphtha','ATF','Kersoene','Diesel','Lubes','Fuel Oil','Bitumen','Petcoke','Others'])
plt.grid(linestyle='dotted')
# line plot is shown below
plt.figure(3)
pltdata2=init_list_of_objects(len(data[0]))
for p in range(len(data[0])):
    for q in range(var):
        pltdata2[p].append(data[q][p])
plt.title('Plot showing the variation of import quantity of Petrol from 2011-18 ',color='blue',fontsize=20)
plt.xlabel('Year',color='blue',fontsize=15)
plt.ylabel('Import Quantity of Petrol',color='blue',fontsize=15)
pltdata2.remove(pltdata2[0])
plt.plot(year,pltdata2[1],'--r',marker='^')
plt.grid(linestyle='dotted')
plt.show()




