import sys
from PyQt5.QtWidgets import QApplication,QDialog
from select import Ui_Form

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.prograW.itemSelectionChanged.connect(self.mostrarseleccion)
        self.show()



    def mostrarseleccion(self):
        lenguajes=self.ui.prograW.selectedItems()
        for lenguaje in list(lenguajes):
            self.ui.lenguajesA.addItem(lenguaje.text())






if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Aplicacion()
    dialogo.show()
    sys.exit(app.exec_())