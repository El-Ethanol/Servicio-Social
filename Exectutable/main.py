from PyQt5.QtCore import pyqtSignal, QThread, QObject
from principal import *
import time        
import test     
from test import *
          
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow): #Ventana Principal
     
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
        self.b1.clicked.connect(self.thread.start)

        # Stop Button action:
        self.b2.clicked.connect(self.stop_thread)
        
        #Other buttons
        
        self.b3.clicked.connect(self.hello)#Presión Actual
        self.b4.clicked.connect(self.hello)#Gráfica
        self.b5.clicked.connect(self.hello)#Guardar Gráfica
        self.b6.clicked.connect(self.hello)#Guardar Datos
        self.r1.clicked.connect(self.hello)#Determinado
        self.r2.clicked.connect(self.hello)#Indeterminado
        

        self.show()

    # When stop_btn is clicked this runs. Terminates the worker and the thread.
     def stop_thread(self):
        self.stop_signal.emit()  # emit the finished signal on stop
        
     def hello(self):
          print("Hello")
       
class Worker(QObject): #Contador
    
    finished = pyqtSignal()  # give worker class a finished signal

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        test.run=True

    def do_work(self):
        s_main()
        self.finished.emit()  # emit the finished signal when the loop is done

    def stop(self):
        test.run= False  # set the run condition to false on stop
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
    
