import sys
import numpy as np
import seaborn as sns
import pyqtgraph as pg
import pyqtgraph.exporters
import math as m
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from pyqtgraph import PlotWidget, plot

x=0
n=0
for i in range(10):
    x=x+i
    print(x)
y=[1,2,3,4]
for i in range(len(y)):
    y[i]=y[i]+x+i
print(y)

t=np.zeros(100)
x=np.zeros(100)
for i in range(len(t)):
    t[i]=i
    x[i]=m.sin(t[i])+m.cos(t[i])+(t[i])

