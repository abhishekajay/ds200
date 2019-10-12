import numpy as np
import matplotlib.pyplot as plt
import sys
import math

filehandle=open("test.csv","r")
#Coili=[]; Coile=[]
#LPGi=[] ; LPGe=[]
#Peti=[] ; Pete=[]
#Napi=[] ; Nape=[]
#Avi=[] ;  Ave=[]
#Keri=[]; Kere=[]
#Diei=[]; Diee=[]
#Lubi=[]; Lube=[]
#Foili=[]; Foile=[]
#Biti=[]; Bite=[]
#Pcokei=[]; Pcokee=[]
#Pothersi=[]; Potherse=[]
year=[]
var=[]
flag=0
count=1
for l in filehandle:
    var=len(l.split(","))-1
    break
var=int(var)
data=[[]]*(var)
data1=[[]]*var
for line in filehandle:
    a=line.split(",")
    if count==1: 
        year=a[1:]
        count=count+1
    if a[0][0]=="T":
        flag=1
    if (count >1 and a[0][0]!="T" and a[0][0]!="N" and flag==0 ):
        data[0].append(a[1])
        count=count+1
    elif a[0][0]!="T" and a[0][0]!="N" and flag==1 :
        data1[0].append(a[1])
        count=count+1
print(data1[0])
# the first scatter plot aims to compare the import and 
# export values of petroleum products between 2011-2018

