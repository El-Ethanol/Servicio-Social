from PyQt5 import QtWidgets        
from PyQt5.QtCore import pyqtSignal, QThread, QObject, QTime, QTimer
from PyQt5.QtWidgets import QMessageBox, QAction
from presiona import *

class WindowPresion(QtWidgets.QMainWindow, Ui_NewWindoe): #Pressure Window
    
    def __init__(self, parent=None):
        super(WindowPresion, self).__init__(parent)
        self.setupUi(self)
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)
        
    def showTime(self):
        current_time=QTime.currentTime()
        label_time=current_time.toString('hh:mm:ss')
        self.label2.setText(label_time)
        
    def closeEvent(self, event):
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
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = WindowPresion()
    window.show()
    app.exec_()