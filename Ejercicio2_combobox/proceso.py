import sys 
from PyQt5.QtWidgets import QDialog,QApplication
from combobox import Ui_Form

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.enviar.clicked.connect(self.enviar)


    def enviar(self):
        #         Aqui consigo el dato                  Aqui consigo el indice del dato  por eso dije checa el dato segun el indice selccionado
        seleccion=self.ui.datos.itemText(self.ui.datos.currentIndex())
        self.ui.label.setText("Lenguaje Selecionado : "+seleccion)




if __name__ == '__main__':
    app=QApplication(sys.argv) 
    dialog=Aplicacion()
    dialog.show()
    sys.exit(app.exec_())

