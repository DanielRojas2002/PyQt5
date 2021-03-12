import sys
from PyQt5.QtWidgets import QDialog,QApplication
from calcu_botones import Ui_Form

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.numero0.clicked.connect(self.respuesta0)
        self.ui.numero1.clicked.connect(self.respuesta1)
        self.ui.numero2.clicked.connect(self.respuesta2)
        self.ui.numero3.clicked.connect(self.respuesta3)
        self.ui.numero4.clicked.connect(self.respuesta4)
        self.ui.numero5.clicked.connect(self.respuesta5)
        self.ui.numero6.clicked.connect(self.respuesta6)
        self.ui.numero7.clicked.connect(self.respuesta7)
        self.ui.numero8.clicked.connect(self.respuesta8)
        self.ui.numero9.clicked.connect(self.respuesta9)
        self.ui.mas.clicked.connect(self.respuestaMas)
        self.ui.menos.clicked.connect(self.respuestaMenos)
        self.ui.multi.clicked.connect(self.respuestaMulti)
        self.ui.division.clicked.connect(self.respuestaDiv)
        self.ui.borraruno.clicked.connect(self.respuestaB)
        self.ui.igual.clicked.connect(self.respuestaIgual)
        self.ui.punto.clicked.connect(self.respuestaPunto)
        self.ui.parentesisizq.clicked.connect(self.respuestaIzq)
        self.ui.parentesisder.clicked.connect(self.respuestaDer)


    def respuesta0(self):
        operacion=self.ui.resultado.text()+"0"
        self.ui.resultado.setText(operacion)

    def respuesta1(self):
        operacion=self.ui.resultado.text()+"1"
        self.ui.resultado.setText(operacion)

    def respuesta2(self):
        operacion=self.ui.resultado.text()+"2"
        self.ui.resultado.setText(operacion)

    def respuesta3(self):
        operacion=self.ui.resultado.text()+"3"
        self.ui.resultado.setText(operacion)


    def respuesta4(self):
        operacion=self.ui.resultado.text()+"4"
        self.ui.resultado.setText(operacion)


    def respuesta5(self):
        operacion=self.ui.resultado.text()+"5"
        self.ui.resultado.setText(operacion)


    def respuesta6(self):
        operacion=self.ui.resultado.text()+"6"
        self.ui.resultado.setText(operacion)

    def respuesta7(self):
        operacion=self.ui.resultado.text()+"7"
        self.ui.resultado.setText(operacion)

    def respuesta8(self):
        operacion=self.ui.resultado.text()+"8"
        self.ui.resultado.setText(operacion)


    def respuesta9(self):
        operacion=self.ui.resultado.text()+"9"
        self.ui.resultado.setText(operacion)

    def respuestaMas(self):
        operacion=self.ui.resultado.text()+"+"
        self.ui.resultado.setText(operacion)


    def respuestaMenos(self):
        operacion=self.ui.resultado.text()+"-"
        self.ui.resultado.setText(operacion)


    def respuestaMulti(self):
        operacion=self.ui.resultado.text()+"*"
        self.ui.resultado.setText(operacion)


    def respuestaDiv(self):
        operacion=self.ui.resultado.text()+"/"
        self.ui.resultado.setText(operacion)


    def respuestaPunto(self):
        operacion=self.ui.resultado.text()+"."
        self.ui.resultado.setText(operacion)

    def respuestaIzq(self):
        operacion=self.ui.resultado.text()+"("
        self.ui.resultado.setText(operacion)

    def respuestaDer(self):
        operacion=self.ui.resultado.text()+")"
        self.ui.resultado.setText(operacion)

    

    def respuestaIgual(self):
        resultado=self.ui.resultado.text()
        try:
            ans=eval(str(resultado))
            self.ui.resultado.setText(str(ans))
        except:
            self.ui.resultado.setText("Error")

    def respuestaB(self):
        text=self.ui.resultado.text()
        self.ui.resultado.setText(text[:len(text)-1])

if __name__=="__main__":
    app=QApplication(sys.argv)
    dialog=Aplicacion()
    dialog.show()
    sys.exit(app.exec_())