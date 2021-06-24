import sys
import os 
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from codigo.progress import Ui_Ventana_Progress


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui=Ui_Ventana_Progress()
        self.ui.setupUi(self)

        self.ui.descargar.clicked.connect(self.simulacion)
        self.ui.progressBar.setValue(0)

    def simulacion(self):
        x=0
        while x<100:
            x+=0.0001
            self.ui.progressBar.setValue(x)


        QMessageBox.information(self,"Mensaje","Descarga Completada",QMessageBox.Ok,QMessageBox.Ok)
        self.ui.progressBar.setValue(0)



if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaPrincipal()
    main.show()
    sys.exit(app.exec_())