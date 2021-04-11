import time, test
from numpy.core.numeric import False_, ones_like
import pyqtgraph as pg
import matplotlib.pyplot as plt
from PresionMain import *
from PyQt5 import QtWidgets        
from PyQt5.QtCore import pyqtSignal, QThread, QObject
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QAction
from principal import *  
from test import *
          
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow): #Main Window
     
     stop_signal = pyqtSignal()
     
     def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(35, 35, 35);") 
        self.count = 0
        self.start = False
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

        # Sensor Buttons:
        self.b1.clicked.connect(self.start_action)#Iniciar Sensor
        self.b25.clicked.connect(self.reset_action)#Reiniciar Sensor
        self.b2.clicked.connect(self.pause_action)#Detener Sensor
        
        #Other buttons  
        self.b3.clicked.connect(self.presionventana)#Presión Actual
        self.b4.clicked.connect(self.grafventana)#Gráfica
        self.b5.clicked.connect(self.guardarg)#Guardar Gráfica
        self.b6.clicked.connect(self.guardard)#Guardar Datos
        self.r1.clicked.connect(self.determinado)#Determinado
        self.r2.clicked.connect(self.indeterminado)#Indeterminado
        
        quit = QAction("Quit", self)#Close
        quit.triggered.connect(self.closeEvent)

        self.show()

    # Definitions
    
     def showTime(self):
        if self.start:
            self.count = self.count+1
            print(self.count)
            time.sleep(1)
            if self.count == tiempo1:
                self.start = False
                
     def start_action(self):
        self.start = True
        if self.count == tiempo1:
            self.start = False
  
     def pause_action(self):
        self.start = False
  
     def reset_action(self):
        self.start = False
        self.count = 0
          
     def presionventana(self):
          self.window = QtWidgets.QMainWindow()
          self.ui1 = WindowPresion()
          self.ui1.setupUi(self.window)
          self.window.show()
     
     def grafventana(self):
          y = [2,4,6,8,10,12,14,16,18,20]
          x = range(0,10)
          plt = pg.plot(x, y, title="Gráfica", pen='r')
          plt.showGrid(x=True,y=True)
          
     def determinado(self):
         global tiempo1,tiempo2
         tiempo1=float(self.l1.text())
         tiempo2=False
         
     def indeterminado(self):
         global tiempo1, tiempo2
         tiempo2=True
         tiempo1=0
          
     def closeEvent(self,event):
          close = QMessageBox()
          close.setWindowTitle("Salir...")
          close.setText("¿Deseas salir?")
          close.setIcon(QMessageBox.Question)
          close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
          close.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(64, 64, 64);")
          close = close.exec()

          if close == QMessageBox.Yes:
             event.accept()
          else:
             event.ignore()
             
     def guardard(self):
          text= QtWidgets.QInputDialog.getText(self, 'Guardar Como:', 'Guardar Como:')   
          if text[1]:
             nombre = text[0]
             print(nombre)        
             
     def guardarg(self):
          text= QtWidgets.QInputDialog.getText(self, 'Guardar Como:', 'Guardar Como:')   
          if text[1]:
             nombre = text[0]
             print(nombre)
           
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
    
