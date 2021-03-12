import sys
from PyQt5.QtWidgets import QDialog,QApplication
from examen_interfaz import Ui_Form

class Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.enviar.clicked.connect(self.info)



    def info(self):
        usuario=self.ui.usuario.text()
        contra=self.ui.contra.text()
        seleccion=self.ui.combo.itemText(self.ui.combo.currentIndex())
        dulce=""
        genero=""
    
        if self.ui.hombre.isChecked()==True:
            genero="Masculino"

        if self.ui.mujer.isChecked()==True:
            genero="Femenino"

        if self.ui.otro.isChecked()==True:
            genero="Otro"

        if self.ui.choco.isChecked()==True:
            dulce="Chocolate,"

        if self.ui.chicle.isChecked()==True:
            dulce=dulce+"Chicle,"

        if self.ui.fresas.isChecked()==True:
            dulce=dulce+"Fresas"

        
        self.ui.resultado.setText(f"Usuario: {usuario}\nContraseña: {contra}\nGenero: {genero}\nDulce: {dulce}\nLenguaje Favorito:{seleccion}")


if __name__=="__main__":
    app=QApplication(sys.argv)
    dialog=Aplicacion()
    dialog.show()
    sys.exit(app.exec_())

