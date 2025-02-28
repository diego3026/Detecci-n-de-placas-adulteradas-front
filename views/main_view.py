# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 601)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(140, 140, 140);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.login_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.login_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 30px 40px;\n"
"border-radius: 20px;\n"
"")
        self.login_frame.setObjectName("login_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.login_frame)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.login_frame)
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(21)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 175 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"padding:0;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.login_frame)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(102, 112, 133);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"padding:0;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(parent=self.login_frame)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"padding:0;\n"
"color: rgb(0, 0, 0);\n"
"margin-bottom:10px;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.login_frame)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit.setStyleSheet("border:1px solid #D0D5DD;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(parent=self.login_frame)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"padding:0;\n"
"color: rgb(0, 0, 0);\n"
"margin-bottom:10px;\n"
"")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.login_frame)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_2.setStyleSheet("border:1px solid #D0D5DD;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.boton_login = QtWidgets.QPushButton(parent=self.login_frame)
        self.boton_login.setMaximumSize(QtCore.QSize(16777215, 100))
        self.boton_login.setBaseSize(QtCore.QSize(0, 0))
        self.boton_login.setStyleSheet("background-color: rgb(94, 90, 219);\n"
"padding:8px 0;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:10px")
        self.boton_login.setObjectName("boton_login")
        self.verticalLayout.addWidget(self.boton_login)
        self.gridLayout.addWidget(self.login_frame, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)
        self.titulo_principal_main = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo_principal_main.sizePolicy().hasHeightForWidth())
        self.titulo_principal_main.setSizePolicy(sizePolicy)
        self.titulo_principal_main.setStyleSheet("padding-top:12px;\n"
"padding-bottom:12px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.titulo_principal_main.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titulo_principal_main.setObjectName("titulo_principal_main")
        self.gridLayout.addWidget(self.titulo_principal_main, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Ingreso al sistema"))
        self.label_3.setText(_translate("MainWindow", "Bienvenido, ingresa tus credenciales"))
        self.label_8.setText(_translate("MainWindow", "Credenciales de usuario"))
        self.label_9.setText(_translate("MainWindow", "Contraseña de usuario"))
        self.boton_login.setText(_translate("MainWindow", "Login"))
        self.titulo_principal_main.setText(_translate("MainWindow", "APLICACIÓN DE MONITORIO DEL SISTEMA DE DETECIÓN DE PLACAS ADULTERADAS"))
