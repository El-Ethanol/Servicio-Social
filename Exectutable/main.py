import time, test
from numpy.core.numeric import False_
import pyqtgraph as pg
import matplotlib.pyplot as plt
from PresionMain import *
from PyQt5 import QtWidgets        
from PyQt5.QtCore import pyqtSignal, QThread, QObject
from PyQt5.QtWidgets import QMessageBox, QAction
from principal import *  
from test import *
          
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow): #Main Window
     
     stop_signal = pyqtSignal()
     
     def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
       
    # Thread:
        self.thread = QThread()
        self.worker = Worker()
        self.stop_signal.connect(self.worker.stop)  # connect stop signal to worker stop method
        self.worker.moveToThread(self.thread)

        self.worker.finished.connect(self.thread.quit)  # connect the workers finished signal to stop thread
        self.worker.finished.connect(self.worker.deleteLater)  # connect the workers finished signal to clean up worker
        self.thread.finished.connect(self.thread.deleteLater)  # connect threads finished signal to clean up thread

        self.thread.started.connect(self.worker.do_work)
        self.thread.finished.connect(self.worker.stop)

        # Start Button action:
        self.b1.clicked.connect(self.thread.start)#Iniciar Sensor
        self.b1.pressed.connect(self.reiniciar)

        # Stop Button action:
        self.b2.clicked.connect(self.stop_thread)#Detener Sensor
        
        #Other buttons  
        self.b3.clicked.connect(self.presionventana)#Presión Actual
        self.b4.clicked.connect(self.grafventana)#Gráfica
        self.b5.clicked.connect(self.prueba)#Guardar Datos
        self.b6.clicked.connect(self.hello)#Guardar Gráfica
        self.r1.clicked.connect(self.determinado)#Determinado
        self.r2.clicked.connect(self.indeterminado)#Indeterminado
        
        quit = QAction("Quit", self)#Preguntar para cerrar
        quit.triggered.connect(self.closeEvent)

        self.show()

    # Definitions
     def stop_thread(self):
        self.stop_signal.emit()
        
     def hello(self):
          print("Hello")
          
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
         global tiempo2
         tiempo2=True
     
     def reiniciar(self):
         test.run=True
         
     def prueba(self):
         print(tiempo1)
         print(tiempo2)
          
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
            
class Worker(QObject): #Counter 
    finished = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        test.run=True

    def do_work(self):
        s_main()
        self.finished.emit() 

    def stop(self):
        test.run= False 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
    
