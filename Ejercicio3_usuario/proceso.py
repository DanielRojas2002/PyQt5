import sys
from PyQt5.QtWidgets import QDialog,QApplication
from usuario import Ui_Form

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.imprimir.clicked.connect(self.imprimir)
        self.show()
    
    def imprimir(self):
        usuario=self.ui.usuario.text()
        contraseña=self.ui.contra.text()
        self.ui.resultado.setText("Usuario : "+usuario+"\n"+"Contraseña : " +contraseña)



if __name__=="__main__":
    app=QApplication(sys.argv)
    dialog=Aplicacion()
    dialog.show()
    sys.exit(app.exec_())

