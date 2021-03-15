from PyQt5.QtWidgets import QApplication,QDialog
import sys
from diagnostico import Ui_Form

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)


        self.ui.listWidget.itemClicked.connect(self.diagnostico)
        self.show()


    def diagnostico(self):
        dato=self.ui.listWidget.currentItem().text()
        self.ui.resultado.setText("Analisis Seleccionado: "+dato)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Aplicacion()
    dialogo.show()
    sys.exit(app.exec_())
