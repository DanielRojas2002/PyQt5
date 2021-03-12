import sys
from PyQt5.QtWidgets import QDialog,QApplication
from calcu_youtube import Ui_Form

class CalculadoraAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.sumar.clicked.connect(self.sumar)
        self.ui.resta.clicked.connect(self.resta)
        self.ui.multi.clicked.connect(self.multiplicacion)
        self.ui.division.clicked.connect(self.division)
    

        self.show()

    def sumar(self):
        try:
            suma=0
            numero1=0
            numero2=0
            if len(self.ui.num1.text())>0 and len(self.ui.num2.text())>0:
                numero1=int(self.ui.num1.text())
                numero2=int(self.ui.num2.text())
                suma=int(numero1+numero2)
                suma=str(suma)
                self.ui.label.setText(f"La Suma es : {suma}")

            else:
                self.ui.label.setText("Ingresa datos en las cajas :)")
        except:
            self.ui.label.setText("Solo se permiten valores numericos :)")



    def resta(self):
        try:
            resta=0
            numero1=0
            numero2=0
            if len (self.ui.num1.text())>0 and len (self.ui.num2.text())>0:
                numero1=int(self.ui.num1.text())
                numero2=int(self.ui.num2.text())
                resta=int(numero1-numero2)
                resta=str(resta)
                self.ui.label.setText(f"La Resta es : {resta}")

            else:
                self.ui.label.setText("Ingresa datos en las cajas :)")
        except:
            self.ui.label.setText("Solo se permiten valores numericos :)")


    def multiplicacion(self):
        try:

            multiplicacion=0
            numero1=0
            numero2=0
            if len (self.ui.num1.text())>0 and len (self.ui.num2.text())>0:
                numero1=int(self.ui.num1.text())
                numero2=int(self.ui.num2.text())
                multiplicacion=int(numero1*numero2)
                multiplicacion=str(multiplicacion)
                self.ui.label.setText(f"La Multiplicacion es : {multiplicacion}")

            else:
                self.ui.label.setText("Ingresa datos en las cajas :)")
        except:
            self.ui.label.setText("Solo se permiten valores numericos :)")
    
    def division(self):
        try:
            division=0
            numero1=0
            numero2=0
            if len (self.ui.num1.text())>0 and len (self.ui.num2.text())>0:
                numero1=int(self.ui.num1.text())
                numero2=int(self.ui.num2.text())
                division=int(numero1/numero2)
                division=str(division)
                self.ui.label.setText(f"La Division es : {division}")
            
            else:
                self.ui.label.setText("Ingresa datos en las cajas :)")
        except:
            self.ui.label.setText("Solo se permiten valores numericos :)")

        



if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialog=CalculadoraAplicacion()
    dialog.show()
    sys.exit(app.exec_())