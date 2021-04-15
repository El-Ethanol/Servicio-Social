from PyQt5 import QtCore, QtGui
import pyqtgraph as pg
import random

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.login_widget = LoginWidget(self)
        self.login_widget.button1.clicked.connect(self.starter)
        self.login_widget.button2.clicked.connect(self.stopper)
        self.central_widget.addWidget(self.login_widget)
        self.setWindowTitle("Gráfica...")
        self.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.start=False
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updater)
        timer.start(100)
        self.data =[0]
        self.curve = self.login_widget.plot.getPlotItem().plot()

    def updater(self):
        if self.start:
            self.data.append(self.data[-1]+0.2*(0.5-random.random()) )
            self.curve.setData(self.data)
        
    def starter(self):
        self.start=True
        
    def stopper(self):
        self.start=False
        

class LoginWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QtGui.QVBoxLayout()
        self.button1 = QtGui.QPushButton('Gráficar segundo a segundo')
        self.button2 = QtGui.QPushButton('Detener')
        self.button1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);")
        self.button2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);")
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.plot = pg.PlotWidget()
        layout.addWidget(self.plot)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()