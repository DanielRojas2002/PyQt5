import sys
from PyQt5.QtWidgets import QDialog,QApplication
from comida import Ui_Form


class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.pastel.toggled.connect(self.info)
        self.ui.helado.toggled.connect(self.info)
        self.ui.pay.toggled.connect(self.info)
        self.ui.galletas.toggled.connect(self.info)

        self.ui.mexicana.toggled.connect(self.info2)
        self.ui.china.toggled.connect(self.info2)
        self.ui.arabe.toggled.connect(self.info2)
        self.ui.italiana.toggled.connect(self.info2)
        self.show()

    def info(self):
        postre=""
        if self.ui.pastel.isChecked()==True:
            postre="es el :Pastel"

        if self.ui.helado.isChecked()==True:
            postre="es el :Helado"

        if self.ui.pay.isChecked()==True:
            postre="es el :Pay"

        if self.ui.galletas.isChecked()==True:
            postre="son las :Galletas"

        self.ui.resultado1.setText("El postre favorito de usted "+postre)

    def info2(self):
        comida=""
        if self.ui.mexicana.isChecked()==True:
            comida="es la :Comida Mexicana"

        if self.ui.china.isChecked()==True:
            comida="es la :Comida China"

        if self.ui.arabe.isChecked()==True:
            comida="es la :Comida Arabe"

        if self.ui.italiana.isChecked()==True:
            comida="es la :Comida Italiana"

        self.ui.resultado2.setText("La Comida favorita de usted "+comida)

if __name__=="__main__":
    app=QApplication(sys.argv)
    dialogo=Aplicacion()
    dialogo.show()
    sys.exit(app.exec_())