# Form implementation generated from reading ui file 'ui/general_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(934, 607)
        Form.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 0 10px")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setStyleSheet("border:none;\n"
"margin-top:10px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../resources/images/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(80, 40))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.general = QtWidgets.QPushButton(parent=self.frame)
        self.general.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.general.setObjectName("general")
        self.verticalLayout.addWidget(self.general)
        self.imagenes = QtWidgets.QPushButton(parent=self.frame)
        self.imagenes.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.imagenes.setObjectName("imagenes")
        self.verticalLayout.addWidget(self.imagenes)
        self.log = QtWidgets.QPushButton(parent=self.frame)
        self.log.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)
        self.informes = QtWidgets.QPushButton(parent=self.frame)
        self.informes.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.informes.setObjectName("informes")
        self.verticalLayout.addWidget(self.informes)
        self.line_2 = QtWidgets.QFrame(parent=self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.desconectarse = QtWidgets.QPushButton(parent=self.frame)
        self.desconectarse.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.desconectarse.setObjectName("desconectarse")
        self.verticalLayout.addWidget(self.desconectarse)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_6.setStyleSheet("border:none;\n"
"background:transparent;")
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../resources/svg/bell-solid-black.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.line_3 = QtWidgets.QFrame(parent=self.frame_3)
        self.line_3.setStyleSheet("color: rgb(118, 118, 118);\n"
"margin: 6px 0;")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.widget = QtWidgets.QWidget(parent=self.frame_3)
        self.widget.setStyleSheet("border:none;")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setStyleSheet("color: rgb(113, 113, 113);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"padding:0;\n"
"padding-left:10px")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_8.setStyleSheet("color: rgb(124, 124, 124);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_9.setLineWidth(0)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.line_4 = QtWidgets.QFrame(parent=self.frame_6)
        self.line_4.setStyleSheet("color: rgb(132, 132, 132);")
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_4.addWidget(self.frame_10)
        self.verticalLayout_4.setStretch(3, 4)
        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(parent=self.frame_9)
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_6.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame_8)
        self.pushButton_8.setStyleSheet("border:none;")
        self.pushButton_8.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\../resources/images/logo_grafica_informe.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(80, 90))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_7.addWidget(self.pushButton_8)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_10.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.frame_7)
        self.tabWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.operaciones_exitosas = QtWidgets.QWidget()
        self.operaciones_exitosas.setObjectName("operaciones_exitosas")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.operaciones_exitosas)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.listView = QtWidgets.QListView(parent=self.operaciones_exitosas)
        self.listView.setStyleSheet("color: rgb(0, 0, 0);")
        self.listView.setObjectName("listView")
        self.verticalLayout_8.addWidget(self.listView)
        self.tabWidget.addTab(self.operaciones_exitosas, "")
        self.operaciones_fallidas = QtWidgets.QWidget()
        self.operaciones_fallidas.setObjectName("operaciones_fallidas")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.operaciones_fallidas)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.listWidget = QtWidgets.QListWidget(parent=self.operaciones_fallidas)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_9.addWidget(self.listWidget)
        self.tabWidget.addTab(self.operaciones_fallidas, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout_5.setStretch(1, 1)
        self.gridLayout.addWidget(self.frame_7, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.verticalLayout_2.addWidget(self.frame_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 17)
        self.verticalLayout_2.setStretch(3, 4)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "general"))
        self.general.setText(_translate("Form", "General"))
        self.imagenes.setText(_translate("Form", "Gestion de imagenes"))
        self.log.setText(_translate("Form", "Logs de aplicacion"))
        self.informes.setText(_translate("Form", "Informes generados"))
        self.desconectarse.setText(_translate("Form", "Desconectarse"))
        self.label_3.setText(_translate("Form", "VISTA GENERAL"))
        self.label_5.setText(_translate("Form", "Superuser"))
        self.label_4.setText(_translate("Form", "Administrador"))
        self.label_2.setText(_translate("Form", "Esta página le muestra el resumen completo de todos los eventos."))
        self.label_8.setText(_translate("Form", "Estadisticas"))
        self.label_9.setText(_translate("Form", "OPERACIONES DE LA APLICACION"))
        self.label.setText(_translate("Form", "Numero de infomes generados"))
        self.label_6.setText(_translate("Form", "3"))
        self.label_10.setText(_translate("Form", "Detalles"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.operaciones_exitosas), _translate("Form", "Operaciones exitosas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.operaciones_fallidas), _translate("Form", "Operaciones fallidas"))
