from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox,QFileDialog
import sys
import os
from ventana_caracter import Ui_Ventana_Caracteres


archivo=""
class VentanaP1(QMainWindow):
    def __init__(self):
        super(VentanaP1,self).__init__()
        self.ui=Ui_Ventana_Caracteres()
        self.ui.setupUi(self)

        
        self.ui.hacer.clicked.connect(self.borrar)

    def borrar(self):
        global archivo
        archivo=self.ui.ruta.text()

        if len(self.ui.ruta.text())>0:
            lista=[]
         
            for raiz, dirs, archivos in os.walk(archivo, topdown=False):    #Demostración de unpacking
                for nombre in archivos:
                    x=nombre
                    print(x)
                    lista.append(x)
           

            for elemento in lista:
                nuevo_nombre=(elemento[1::])
                fin=archivo + "\\"+elemento
                os.rename(fin,archivo+"\\"+nuevo_nombre)
                self.ui.resultado.setText("Ya se realizo el Cambio")

        else:
            self.ui.resultado.setText("Ingrese la ruta")
  

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaP1()
    main.show()
    sys.exit(app.exec_())  
      