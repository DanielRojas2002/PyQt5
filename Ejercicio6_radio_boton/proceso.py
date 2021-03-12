import sys
from PyQt5.QtWidgets import QDialog,QApplication
from tipo_vuelo import Ui_Form

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.rbprimera.toggled.connect(self.info1)
        self.ui.rbsegunda.toggled.connect(self.info2)
        self.ui.rbnegocio.toggled.connect(self.info3)
        self.ui.rbfamiliar.toggled.connect(self.info4)
        self.show()

    
    def info1(self):
        costo=0
        if self.ui.rbprimera.isCheckable() == True:
            costo=str(4200)
            self.ui.resultado.setText("El costo del boleto para la Primera Clase es : $"+ costo)

    def info2(self):
        if self.ui.rbsegunda.isCheckable() == True:
            self.ui.resultado.setText("El costo del boleto para la Segunda Clase es : $3800 pesos")

    def info3(self):
        if self.ui.rbnegocio.isCheckable()==True:
            self.ui.resultado.setText("El costo del boleto para la Clase Negocio es : $2800 pesos")
            
    def info4(self):
        if self.ui.rbfamiliar.isCheckable()==True:
            self.ui.resultado.setText("El costo del boleto para la Clase Familiar es : $2000 pesos")



if __name__ == "__main__":
    app=QApplication(sys.argv)
    dialog=Aplicacion()
    dialog.show()
    sys.exit(app.exec_())