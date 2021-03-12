# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tipo_de_vuelo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 199)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.rbprimera = QtWidgets.QRadioButton(Form)
        self.rbprimera.setGeometry(QtCore.QRect(40, 80, 91, 21))
        self.rbprimera.setObjectName("rbprimera")
        self.rbnegocio = QtWidgets.QRadioButton(Form)
        self.rbnegocio.setGeometry(QtCore.QRect(40, 120, 101, 17))
        self.rbnegocio.setObjectName("rbnegocio")
        self.rbfamiliar = QtWidgets.QRadioButton(Form)
        self.rbfamiliar.setGeometry(QtCore.QRect(250, 120, 101, 17))
        self.rbfamiliar.setObjectName("rbfamiliar")
        self.rbsegunda = QtWidgets.QRadioButton(Form)
        self.rbsegunda.setGeometry(QtCore.QRect(250, 80, 101, 17))
        self.rbsegunda.setObjectName("rbsegunda")
        self.pregunta = QtWidgets.QLineEdit(Form)
        self.pregunta.setGeometry(QtCore.QRect(30, 20, 321, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pregunta.setFont(font)
        self.pregunta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pregunta.setAlignment(QtCore.Qt.AlignCenter)
        self.pregunta.setObjectName("pregunta")
        self.resultado = QtWidgets.QLabel(Form)
        self.resultado.setGeometry(QtCore.QRect(30, 170, 341, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resultado.setFont(font)
        self.resultado.setFrameShape(QtWidgets.QFrame.Box)
        self.resultado.setText("")
        self.resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.resultado.setObjectName("resultado")
        self.imagen = QtWidgets.QLabel(Form)
        self.imagen.setGeometry(QtCore.QRect(160, 80, 71, 61))
        self.imagen.setFrameShape(QtWidgets.QFrame.Box)
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap("multimedia/avion.jpg"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rbprimera.setText(_translate("Form", "Primera Clase"))
        self.rbnegocio.setText(_translate("Form", "Clase Negocio"))
        self.rbfamiliar.setText(_translate("Form", "Clase Familiar"))
        self.rbsegunda.setText(_translate("Form", "Segunda Clase"))
        self.pregunta.setText(_translate("Form", "¿Que plan de vuelo deseas adquirir?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
