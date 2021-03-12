import sys
from PyQt5.QtWidgets import QDialog,QApplication
from medicion import Ui_Form


class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.scrollA.valueChanged.connect(self.mostrarA)
        self.ui.scrollC.valueChanged.connect(self.mostrarC)
        self.ui.scrollAR.valueChanged.connect(self.mostrarAr)
        self.ui.scrollP.valueChanged.connect(self.mostrarP)

    def mostrarA(self,valor):
        self.ui.resultadoAzu.setText("Nivel del Azucar: {}".format(valor))

    def mostrarC(self,valor):
        self.ui.resultadoC.setText("Nivel del Colesterol: {}".format(valor))

    def mostrarAr(self,valor):
        self.ui.resultadoArt.setText("Nivel Arterial: {}".format(valor))

    def mostrarP(self,valor):
        self.ui.resultadoP.setText("Nivel del Pulso: {}".format(valor))



if __name__ =='__main__':
    app=QApplication(sys.argv)
    dialogo=Aplicacion()
    dialogo.show()
    sys.exit(app.exec_())
