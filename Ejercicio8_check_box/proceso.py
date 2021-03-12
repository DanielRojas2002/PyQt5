import sys
from PyQt5.QtWidgets import QDialog,QApplication
from pizzeria import Ui_Form

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        
        self.ui.precio.setText("Precio Normal de la Pizza : $"+str(80)+" pesos")

        self.ui.Peperoni.stateChanged.connect(self.info)
        self.ui.aceitunas.stateChanged.connect(self.info)
        self.ui.tocino.stateChanged.connect(self.info)
        self.ui.chile.stateChanged.connect(self.info)
        self.ui.chile2.stateChanged.connect(self.info)
        self.ui.Jamon.stateChanged.connect(self.info)
        self.ui.Queso.stateChanged.connect(self.info)
        self.ui.pina.stateChanged.connect(self.info)
        self.show()

    def info(self):
        preciobase=80
        ingrediente=""
        if self.ui.Peperoni.isChecked()==True:
            preciobase=preciobase+10
            ingrediente="Peperoni,"
        
        if self.ui.aceitunas.isChecked()==True:
            preciobase=preciobase+5
            ingrediente=ingrediente+"Aceitunas,"

        if self.ui.tocino.isChecked()==True:
           preciobase=preciobase+15
           ingrediente=ingrediente+"Tocino,"

        if self.ui.chile.isChecked()==True:
            preciobase=preciobase+10
            ingrediente=ingrediente+"Chile Jalapeño,"

        if self.ui.chile2.isChecked()==True:
            preciobase=preciobase+10
            ingrediente=ingrediente+"Chile Morron,"+"\n"

        if self.ui.Jamon.isChecked()==True:
            preciobase=preciobase+20
            ingrediente=ingrediente+"Jamon,"

        if self.ui.Queso.isChecked()==True:
            preciobase=preciobase+25
            ingrediente=ingrediente+"Queso,"

        if self.ui.pina.isChecked()==True:
            preciobase=preciobase+10
            ingrediente=ingrediente+"Piña,"


        self.ui.precio.setText("Precio de la Pizza : $"+str(preciobase)+" pesos")
        self.ui.seleccion.setText("Ingredientes Seleccionados:"+"\n"+ingrediente)
            
            
        


if __name__=='__main__':
    app=QApplication(sys.argv)
    dialogo=Aplicacion()
    dialogo.show()
    sys.exit(app.exec_())