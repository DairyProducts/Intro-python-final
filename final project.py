#IMPORTANT!! THIS IS AN OUTDATED VERSION OF THE CODE. THE AREA UNDER THE CURVE IS A POSITIVE SCALAR-LIKE VALUE. SEARCH THE REPOSITORY FOR AN UPDATED VERSION.
#This code probably won't run on your local machine.
#Change the path on lines 11 and 12 to the file location for dataX and dataY respectively.
import math
import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy import trapz
from array import *
x=[]
y=[]
datax=open('C:/Users/2007d/Desktop/Intro-python-final-master/dataX.csv')
datay=open('C:/Users/2007d/Desktop/Intro-python-final-master/dataY.csv')
datax=csv.reader(datax)
datay=csv.reader(datay)
for rows in datax:
    float(rows[0])
    x.append(float(rows[0]))
    W=float(rows[0])
    #print(W)
    #print(float(rows[0]))
for rows in datay:
    float(rows[0])
    y.append(float(rows[0]))
    H=float(rows[0])
    #print(H)
    #print(float(rows[0]))
Atot=0
for b in range(0,1001):
    #print('b=',b)
    #print('x[b]=',x[b])
    #print('x[b-1]=',x[b-1])
    #print('x[b]-x[b-1]=',x[b]-x[b-1])
    #print('y[b]',y[b])
    #print('(x[b]-x[b-1])*y[b]',(x[b]-x[b-1])*y[b])
    A=(x[b]-x[b-1])*y[b]
    if A<0:
        Atot=Atot-A
    else:
        Atot=Atot+A
print('Answer: ',Atot)
input('Press ENTER to open graph.')
plt.plot(x,y)
plt.show()
