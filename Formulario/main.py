import sys
import os 
import pandas as pd
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from codigo.FORMS import Ui_Ventana_Formulario


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui=Ui_Ventana_Formulario()
        self.ui.setupUi(self)

        self.ui.ragistrar.clicked.connect(self.registro)
        
        
    def registro(self):
        nombre=str(self.ui.entradanombre.text())
        apellido=str(self.ui.entradaapellido.text())
        telefono=str(self.ui.entradatel.text())
        correo=str(self.ui.entradacorreo.text())
        edad=str(self.ui.edad.value())

        datogenero=""
        if self.ui.M.isChecked()==True:
            datogenero="Masculino"

        if self.ui.F.isChecked()==True:
            datogenero="Femenino"


        try:
            if len(nombre)>0 and len(apellido)>0 and len(telefono)>0 and len(correo)>0 and len(datogenero)>0 and len(edad)>0:
                try:
                    if nombre.isdigit():
                        x="z"+1
                    
                    else:
                        puerta=1

                    if apellido.isdigit():
                        x="z"+1

                    else:
                        puerta=1

                    if telefono.isdigit():
                        puerta=1

                    else:
                        puerta=0
                        QMessageBox.warning(self,"Mensaje","El Telefono es numerico",QMessageBox.Ok,QMessageBox.Ok)

                    if "@" in correo:
                        puerta=1

                    else:
                        QMessageBox.warning(self,"Mensaje","Ingrese bien su correo",QMessageBox.Ok,QMessageBox.Ok)
                        puerta=0

                    if puerta==1:
                        dicc={}
                        listanom=[]
                        listaape=[]
                        listatel=[]
                        listacorreo=[]
                        listaedad=[]
                        listagenero=[]

                        listanom.append(nombre)
                        listaape.append(apellido)
                        listatel.append(telefono)
                        listacorreo.append(correo)
                        listaedad.append(edad)
                        listagenero.append(datogenero)

                        dicc["Nombre"]=listanom
                        dicc["Apellido"]=listaape
                        dicc["Telefono"]=listatel
                        dicc["Correo"]=listacorreo
                        dicc["Edad"]=listaedad
                        dicc["Genero"]=listagenero
                        
                        
                        df=pd.DataFrame(dicc)
                        
                        ruta="Formulario/datos/DATOS.csv"
                        df.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
                        QMessageBox.information(self,"Mensaje","Registro Satisfactorio",QMessageBox.Ok,QMessageBox.Ok)

                        self.ui.entradanombre.clear()
                        self.ui.entradaapellido.clear()
                        self.ui.entradatel.clear()
                        self.ui.entradacorreo.clear()
       

                except:
                    QMessageBox.warning(self,"Mensaje","Respete el tipo de Dato",QMessageBox.Ok,QMessageBox.Ok)
                    puerta=0
         
            else:
                QMessageBox.warning(self,"Mensaje","Tienes que ingresar todos tus datos",QMessageBox.Ok,QMessageBox.Ok)

        except:
            pass

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaPrincipal()
    main.show()
    sys.exit(app.exec_())