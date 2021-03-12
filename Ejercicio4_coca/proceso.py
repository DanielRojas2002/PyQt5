import sys
from PyQt5.QtWidgets import QDialog,QApplication
from primera_app import Ui_form

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_form()
        self.ui.setupUi(self)
        self.numero=0

        self.ui.suma.clicked.connect(self.sumar)
        self.ui.resta.clicked.connect(self.resta)

    def sumar(self):
        self.numero=self.numero+1
        self.ui.contador.setText(str(self.numero))

    def resta(self):
        if self.numero<=0:
            self.numero=0
            self.ui.contador.setText(str(self.numero))
        else:
            self.numero=self.numero-1
            self.ui.contador.setText(str(self.numero))


if __name__ == '__main__':
    app=QApplication(sys.argv) 
    dialog=Aplicacion()
    dialog.show()
    sys.exit(app.exec_())

