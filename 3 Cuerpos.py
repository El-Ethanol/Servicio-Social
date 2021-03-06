import sys
import numpy as np
import seaborn as sns
import pyqtgraph as pg
import pyqtgraph.exporters
import math as m
import os
from numpy import linalg as la
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

def RK4(f,x0,t0,tf,h): #Necesita una función, un vector de condiciones iniciales, un intervalo de tiempo y el paso. 
    s=range(t0,tf,h)
    n=len(s)
    s.append(tf+h) #Aumentamos un término extra al vector para tener la misma cantidad de entradas que los vectores de más abajo.
    m=len(x0)
    xs=[np.zeros(m)] 
    for i in range(n):
        xs.append(np.zeros(m)) #Construimos un vector de vectores de zeros de longitud n con m zeros en él.
    xs[1]=x0 
    for i in range(n):
        k1=h*f(s[i],xs[i]) #Definimos los pasos del metodo de R-K.
        k2=h*f(s[i]+0.5*h,xs[i]+0.5*k1)
        k3=h*f(s[i]+0.5*h,xs[i]+0.5*k2)
        k4=h*f(s[i]+h,xs[i]+k3)
        xs[i+1]=xs[i]+(k1+2*k2+2*k3+k4)/6
    return s,xs #Regresamos el vector del tiempo y los vectores solución. 

def rect(x): #Definimos esta función para realizar las estelas de las partículas en las animaciones.
    if x>=0:
        return x
    else:
        return 0

def TresCuerpos1(m1,m2,m3):
    def f1(t,x):
        r1=[x[1],x[3]] #Definimos los 3 vectores que (x1,y1), (x2,y2) y (x3,y3)
        r2=[x[5],x[7]]
        r3=[x[9],x[11]]
        r12=la.norm(r1-r2) #Se calculan las normas para abreviar redacción.
        r13=la.norm(r1-r3)
        r23=la.norm(r2-r3)
        x1=x[2] #Construimos el sistema de ecuaciones que describimos arriba. 
        vx1=m2*(x[5]-x[1])/r12^3+m3*(x[9]-x[1])/r13^3
        y1=x[4]
        vy1=m2*(x[7]-x[3])/r12^3+m3*(x[11]-x[3])/r13^3
        x2=x[6]
        vx2=m1*(x[1]-x[5])/r12^3+m3*(x[9]-x[5])/r23^3
        y2=x[8]
        vy2=m1*(x[3]-x[7])/r12^3+m3*(x[11]-x[7])/r23^3
        x3=x[10]
        vx3=m1*(x[1]-x[9])/r13^3+m2*(x[5]-x[9])/r23^3
        y3=x[12]
        vy3=m1*(x[3]-x[11])/r13^3+m2*(x[7]-x[11])/r23^3
        return [x1,vx1,y1,vy1,x2,vx2,y2,vy2,x3,vx3,y3,vy3] #Regresamos el vector de posiciones y velocidades.
    return f1
