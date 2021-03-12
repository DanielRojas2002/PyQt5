import sys
from PyQt5.QtWidgets import QDialog,QApplication
from ropa import Ui_Form


class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.sb1.editingFinished.connect(self.playera)
        self.ui.sb2.editingFinished.connect(self.pantalon)
        self.ui.totalboton.clicked.connect(self.total)


    def playera(self):
        
        precio=50
        cantidad=self.ui.sb1.value()
        operacion=precio*cantidad
        self.ui.resultado1.setText(str(operacion))

    def pantalon(self):
        precio=100
        cantidad=self.ui.sb2.value()
        operacion=precio*cantidad
        self.ui.resultado2.setText(str(operacion))

    def total(self):
        a=int(self.ui.resultado1.text())
        b=int(self.ui.resultado2.text())
        x=a+b
        self.ui.total.setText("TOTAL:\n"+str(x))




    

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Aplicacion()
    dialogo.show()
    sys.exit(app.exec_())