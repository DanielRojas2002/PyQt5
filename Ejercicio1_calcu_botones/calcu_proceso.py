import sys
from PyQt5.QtWidgets import QDialog,QApplication
from calcu_simple import Ui_Form

class CalculadoraAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.boton0.clicked.connect(self.btn0)
        self.ui.boton1.clicked.connect(self.btn1)

        self.show()


    def btn0(self):
        botoncero="0"
        self.ui.Resultado.setText(str(botoncero))

    def btn1(self):
        botonuno="1"
        self.ui.Resultado.setText(str(botonuno))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialog=CalculadoraAplicacion()
    dialog.show()
    sys.exit(app.exec_())
