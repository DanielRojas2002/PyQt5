# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana_Formulario(object):
    def setupUi(self, Ventana_Formulario):
        Ventana_Formulario.setObjectName("Ventana_Formulario")
        Ventana_Formulario.resize(288, 460)
        Ventana_Formulario.setMaximumSize(QtCore.QSize(288, 460))
        self.centralwidget = QtWidgets.QWidget(Ventana_Formulario)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy)
        self.img.setMaximumSize(QtCore.QSize(250, 200))
        self.img.setFrameShape(QtWidgets.QFrame.Box)
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("Formulario/img/hojaypluma.jpg"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.verticalLayout_2.addWidget(self.img)
        self.verticalLayout.addWidget(self.frame_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(5, 9, 5, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.entradatel = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entradatel.sizePolicy().hasHeightForWidth())
        self.entradatel.setSizePolicy(sizePolicy)
        self.entradatel.setMaxLength(13)
        self.entradatel.setClearButtonEnabled(True)
        self.entradatel.setObjectName("entradatel")
        self.gridLayout.addWidget(self.entradatel, 2, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        self.M = QtWidgets.QRadioButton(self.frame)
        self.M.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.M.setObjectName("M")
        self.gridLayout.addWidget(self.M, 5, 2, 1, 1)
        self.lblcorreo = QtWidgets.QLabel(self.frame)
        self.lblcorreo.setObjectName("lblcorreo")
        self.gridLayout.addWidget(self.lblcorreo, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 4, 1, 1)
        self.lbledad = QtWidgets.QLabel(self.frame)
        self.lbledad.setObjectName("lbledad")
        self.gridLayout.addWidget(self.lbledad, 4, 0, 1, 1)
        self.entradacorreo = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entradacorreo.sizePolicy().hasHeightForWidth())
        self.entradacorreo.setSizePolicy(sizePolicy)
        self.entradacorreo.setMaxLength(50)
        self.entradacorreo.setClearButtonEnabled(True)
        self.entradacorreo.setObjectName("entradacorreo")
        self.gridLayout.addWidget(self.entradacorreo, 3, 2, 1, 2)
        self.entradanombre = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entradanombre.sizePolicy().hasHeightForWidth())
        self.entradanombre.setSizePolicy(sizePolicy)
        self.entradanombre.setMaxLength(50)
        self.entradanombre.setClearButtonEnabled(True)
        self.entradanombre.setObjectName("entradanombre")
        self.gridLayout.addWidget(self.entradanombre, 0, 2, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        self.lblapellido = QtWidgets.QLabel(self.frame)
        self.lblapellido.setObjectName("lblapellido")
        self.gridLayout.addWidget(self.lblapellido, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 5, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 1, 1, 1)
        self.F = QtWidgets.QRadioButton(self.frame)
        self.F.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.F.setObjectName("F")
        self.gridLayout.addWidget(self.F, 5, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 4, 1, 1)
        self.entradaapellido = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entradaapellido.sizePolicy().hasHeightForWidth())
        self.entradaapellido.setSizePolicy(sizePolicy)
        self.entradaapellido.setMaxLength(60)
        self.entradaapellido.setClearButtonEnabled(True)
        self.entradaapellido.setObjectName("entradaapellido")
        self.gridLayout.addWidget(self.entradaapellido, 1, 2, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 2, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 4, 1, 1)
        self.lblsexo = QtWidgets.QLabel(self.frame)
        self.lblsexo.setObjectName("lblsexo")
        self.gridLayout.addWidget(self.lblsexo, 5, 0, 1, 1)
        self.lblnom = QtWidgets.QLabel(self.frame)
        self.lblnom.setObjectName("lblnom")
        self.gridLayout.addWidget(self.lblnom, 0, 0, 1, 1)
        self.ragistrar = QtWidgets.QPushButton(self.frame)
        self.ragistrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ragistrar.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(188, 191, 200);\n"
"}")
        self.ragistrar.setObjectName("ragistrar")
        self.gridLayout.addWidget(self.ragistrar, 6, 3, 1, 2)
        self.lbltelefono = QtWidgets.QLabel(self.frame)
        self.lbltelefono.setObjectName("lbltelefono")
        self.gridLayout.addWidget(self.lbltelefono, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 4, 4, 1, 1)
        self.edad = QtWidgets.QSpinBox(self.frame)
        self.edad.setMinimum(15)
        self.edad.setObjectName("edad")
        self.gridLayout.addWidget(self.edad, 4, 2, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.verticalLayout.addWidget(self.groupBox)
        Ventana_Formulario.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ventana_Formulario)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Formulario)

    def retranslateUi(self, Ventana_Formulario):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Formulario.setWindowTitle(_translate("Ventana_Formulario", "Formulario"))
        self.groupBox.setTitle(_translate("Ventana_Formulario", "Registro:"))
        self.M.setText(_translate("Ventana_Formulario", "Masculino"))
        self.lblcorreo.setText(_translate("Ventana_Formulario", "Corrreo"))
        self.lbledad.setText(_translate("Ventana_Formulario", "Edad"))
        self.lblapellido.setText(_translate("Ventana_Formulario", "Apellidos"))
        self.F.setText(_translate("Ventana_Formulario", "Femenino"))
        self.lblsexo.setText(_translate("Ventana_Formulario", "Sexo"))
        self.lblnom.setText(_translate("Ventana_Formulario", "Nombre"))
        self.ragistrar.setText(_translate("Ventana_Formulario", "REGISTRAR"))
        self.lbltelefono.setText(_translate("Ventana_Formulario", "Telefono"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Formulario = QtWidgets.QMainWindow()
    ui = Ui_Ventana_Formulario()
    ui.setupUi(Ventana_Formulario)
    Ventana_Formulario.show()
    sys.exit(app.exec_())
