# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 517)
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 368, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(85, 255, 127);\n"
"background-color: rgb(56, 56, 56);")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 100, 291, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.r1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.r1.setStyleSheet("color: rgb(255, 255, 255);")
        self.r1.setObjectName("r1")
        self.horizontalLayout_2.addWidget(self.r1)
        self.l1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.l1.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"color: rgb(255, 255, 255);")
        self.l1.setObjectName("l1")
        self.horizontalLayout_2.addWidget(self.l1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.r2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.r2.setStyleSheet("color: rgb(255, 255, 255);")
        self.r2.setObjectName("r2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.r2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 280, 161, 100))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.b3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);")
        self.b3.setObjectName("b3")
        self.verticalLayout.addWidget(self.b3)
        self.b4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.b4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);")
        self.b4.setObjectName("b4")
        self.verticalLayout.addWidget(self.b4)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 400, 371, 61))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b6 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.b6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);")
        self.b6.setObjectName("b6")
        self.horizontalLayout_3.addWidget(self.b6)
        self.b5 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.b5.setStyleSheet("background-color: rgb(56, 56, 56);\n"
"color: rgb(255, 255, 255);")
        self.b5.setObjectName("b5")
        self.horizontalLayout_3.addWidget(self.b5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 251, 24))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color: rgb(85, 255, 127);")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(66, 190, 361, 67))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b1 = QtWidgets.QPushButton(self.widget)
        self.b1.setStyleSheet("background-color: rgb(56, 56, 56);\n"
"color: rgb(255, 255, 255);")
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)
        self.b2 = QtWidgets.QPushButton(self.widget)
        self.b2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);")
        self.b2.setObjectName("b2")
        self.horizontalLayout.addWidget(self.b2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.b25 = QtWidgets.QPushButton(self.widget)
        self.b25.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);")
        self.b25.setObjectName("b25")
        self.verticalLayout_2.addWidget(self.b25)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuardar_Datos_cvs = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Datos_cvs.setObjectName("actionGuardar_Datos_cvs")
        self.actionGuardas_Gr_fica_png = QtWidgets.QAction(MainWindow)
        self.actionGuardas_Gr_fica_png.setObjectName("actionGuardas_Gr_fica_png")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sensor de Presión"))
        self.label.setText(_translate("MainWindow", "Sensor de Presión"))
        self.r1.setText(_translate("MainWindow", "Determinado:"))
        self.label_3.setText(_translate("MainWindow", "Segundos"))
        self.r2.setText(_translate("MainWindow", "Indeterminado"))
        self.b3.setText(_translate("MainWindow", "Presión Actual"))
        self.b4.setText(_translate("MainWindow", "Gráfica"))
        self.b6.setText(_translate("MainWindow", "Guardar datos (.cvs)"))
        self.b5.setText(_translate("MainWindow", "Guardar Gráfica (.png)"))
        self.label_2.setText(_translate("MainWindow", "Tiempo de recolección:"))
        self.b1.setText(_translate("MainWindow", "Iniciar Sensor"))
        self.b2.setText(_translate("MainWindow", "Pausar Sensor"))
        self.b25.setText(_translate("MainWindow", "Reiniciar Sensor"))
        self.actionGuardar_Datos_cvs.setText(_translate("MainWindow", "Guardar Datos (.cvs)"))
        self.actionGuardas_Gr_fica_png.setText(_translate("MainWindow", "Guardas Gráfica (.png)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
