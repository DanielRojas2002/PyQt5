import sys
from PyQt5.QtWidgets import QApplication, QLCDNumber,QMainWindow,QMessageBox,QLCDNumber
from codigo.LCD import Ui_VentanaLCD


numero=0
longitud=0

class VentanaP1(QMainWindow):
    def __init__(self):
        super(VentanaP1,self).__init__()
        self.ui=Ui_VentanaLCD()
        self.ui.setupUi(self)

        self.ui.botonpasar.clicked.connect(self.pasar)

        self.ui.decimal.clicked.connect(self.dec)
        self.ui.binario.clicked.connect(self.bin)
        self.ui.octagonal.clicked.connect(self.oct)
        self.ui.hexadecimal.clicked.connect(self.hexa)
        

        
    def pasar(self):
        global numero
        global longitud
        try:
            longitud=len(self.ui.entrada.text())
           
            if longitud>0:
                numero=int(self.ui.entrada.text())
                self.ui.pantalla.display(str(numero))
                
  
            else:
                QMessageBox.warning(self,"Mensaje","Ingrese el Numero a convertir",QMessageBox.Ok,QMessageBox.Ok)
        except:
            QMessageBox.warning(self,"Mensaje","Solo se perimiten Numeros",QMessageBox.Ok,QMessageBox.Ok)

    def dec(self):
        global numero
        global longitud
        if longitud>0:
            self.ui.pantalla.setDigitCount(longitud)
            self.ui.pantalla.setMode(QLCDNumber.Dec)
        else:
            self.ui.pantalla.display(str(0))
            QMessageBox.warning(self,"Mensaje","Ingrese el Numero a convertir",QMessageBox.Ok,QMessageBox.Ok)


    def bin(self):
        global numero
        global longitud
        if longitud>0:
            self.ui.pantalla.setDigitCount(30)
            self.ui.pantalla.setMode(QLCDNumber.Bin)

        else:
            self.ui.pantalla.display(str(0))
            QMessageBox.warning(self,"Mensaje","Ingrese el Numero a convertir",QMessageBox.Ok,QMessageBox.Ok)
        
    def oct(self):
        global numero
        global longitud
        if longitud>0:
            self.ui.pantalla.setDigitCount(longitud)
            self.ui.pantalla.setMode(QLCDNumber.Oct)

        else:
            self.ui.pantalla.display(str(0))
            QMessageBox.warning(self,"Mensaje","Ingrese el Numero a convertir",QMessageBox.Ok,QMessageBox.Ok)


    def hexa(self):
        global numero
        global longitud
        if longitud>0:
            self.ui.pantalla.setDigitCount(longitud)
            self.ui.pantalla.setMode(QLCDNumber.Hex)

        else:
            self.ui.pantalla.display(str(0))
            QMessageBox.warning(self,"Mensaje","Ingrese el Numero a convertir",QMessageBox.Ok,QMessageBox.Ok)







if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaP1()
    main.show()
    sys.exit(app.exec_())