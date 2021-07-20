import pywhatkit as what
import pyautogui as pg
import time
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from datetime import datetime


from codigo.ventana_whats import Ui_Ventana_Principal

lada=""
numero=""
mensaje=""
tipo=""
hora=""
minuto=""
contadorvalidacion=""
def mandar(lada,numero,mensaje,tipo,hora,minuto,contadorvalidacion):
    if len(lada)>1 and len(numero)==10 and len(mensaje)>0:
        numerocompleto=lada+numero
        print(numerocompleto)
        now = datetime.now()
        horacompu=now.hour
        mincompu=now.minute
        tiempocompleto=hora+":"+minuto+" "+tipo
        
        if tipo=="PM":
            hora=int(hora)+12
            print("aqui")

        if contadorvalidacion==0:
            try:
                hora=int(hora)
                minuto=int(minuto)
                minuto=minuto
                what.sendwhatmsg(numerocompleto,mensaje,hora,minuto,40)
                time.sleep(5)
                pg.press('enter')
            except:
                pass

class VentanaP1(QMainWindow):
    def __init__(self):
        super(VentanaP1,self).__init__()
        self.ui=Ui_Ventana_Principal()
        self.ui.setupUi(self)
        
        self.ui.hacer.clicked.connect(self.enviar)
        self.ui.errorocorrecto.setText("No Cierre esta ventana")

    def enviar(self):
        global lada
        global numero
        global mensaje
        global tipo
        global hora
        global minuto
        global contadorvalidacion    
        
        lada=self.ui.lada.text()
        if "+" not in lada:
            contador=0
            lista=[]
            for x in lada:
                if contador==0:
                    lista.append("+")
                    contador=contador+1

                lista.append(x)
            lada=""
            for x in lista:
                lada=lada+x

        numero=self.ui.tel.text()
        mensaje=self.ui.textEdit.toPlainText()
        tiempo=self.ui.tiempo.text()

        hora=tiempo[0:2]
        minuto=tiempo[3:5]
        tipo=tiempo[5::]
        now = datetime.now()
        horacompu=now.hour
        mincompu=now.minute
        contadorvalidacion=0
        

        characters=" ."
        for x in range(len(characters)):
            tipo = tipo.replace(characters[x],"")

        if int(hora)<int(horacompu) and int(minuto)<int(mincompu):
            print("aca")
            QMessageBox.warning(self,"Error","Ya paso esa hora",QMessageBox.Ok,QMessageBox.Ok)
            contadorvalidacion=1

        else:

            if len(lada)>1 and len(numero)==10 and len(mensaje)>0:
                mandar(lada,numero,mensaje,tipo,hora,minuto,contadorvalidacion)
            else:
                QMessageBox.warning(self,"Error","Necesita poner la lada de tu pais y el numero",QMessageBox.Ok,QMessageBox.Ok)

       

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaP1()
    main.show()
    sys.exit(app.exec_())




            
    







