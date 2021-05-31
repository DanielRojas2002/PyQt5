import sys
from plyer import notification
import datetime
import time 
import pandas as pd 
import os 
from os import remove
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem
from codigo.Ventana_Principal import Ui_Ventana_Padre
from codigo.Ventana_Registrar import Ui_VentanaRegistrarTarea
from codigo.Ventana_Recordatorio import Ui_Ventana_Recordatorio
from codigo.Ventana_Visualizador import Ui_Ventana_Visualizadora
from codigo.Ventana_eliminador import Ui_Ventana_Eliminar

recordatorio=0


class VentanaP1(QMainWindow):
    def __init__(self):
        super(VentanaP1,self).__init__() 
        self.ui=Ui_Ventana_Padre()
        self.ui.setupUi(self)
        self.ui.doit.clicked.connect(self.abrirVentanaCrear)
        
         
    def abrirVentanaCrear(self):
        if self.ui.newhw.isChecked()==True:
            self.hide()
            otraventana=VentanaAgregar(self)
            otraventana.show()

        elif self.ui.watchhw.isChecked()==True:
            self.hide()
            otraventana=VentanaMirar(self)
            otraventana.show()

        elif self.ui.rememberhw.isChecked()==True:
            self.hide()
            otraventana=VentanaRecordar(self)
            otraventana.show()
        
        elif self.ui.deletehw.isChecked()==True:
            self.hide()
            otraventana=VentanaEliminar(self)
            otraventana.show()

    
        
        
class VentanaAgregar(QMainWindow):
    def __init__(self,parent=None):
       super(VentanaAgregar,self).__init__(parent) 
       self.ui=Ui_VentanaRegistrarTarea()
       self.ui.setupUi(self)
       self.ui.exito.setText("")
       


       self.ui.regresar.clicked.connect(self.atras)
       self.ui.doit.clicked.connect(self.registrar)

    def registrar(self):
        ahora=datetime.datetime.now()
        ahora1=str(ahora.strftime('%d/%m/%Y'))

        if len(self.ui.tarea.toPlainText())==0:
            self.ui.exito.setText("Ingrese una Tarea")


        else:
            diccionariooriginal={}
            listafecha=[]
            listatarea=[]
            

            tarea=self.ui.tarea.toPlainText()
            listafecha.append(ahora1)
            listatarea.append(tarea)
            diccionariooriginal["FECHA"]=listafecha
            diccionariooriginal["TAREA"]=listatarea
            diccionario2=pd.DataFrame(diccionariooriginal)
            ruta="Procesador de Tareas/archivos/Tareas.csv"

            diccionario2.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
           
            
            self.ui.exito.setText("Tarea Registrada")
            self.ui.tarea.clear()
           

    def atras(self):
        self.parent().show()
        self.close()
    

class VentanaMirar(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaMirar,self).__init__(parent)
        self.ui=Ui_Ventana_Visualizadora()
        self.ui.setupUi(self)

        self.ui.regresar.clicked.connect(self.atras)
        try:
            tareas=pd.read_csv("Procesador de Tareas/archivos/Tareas.csv")
            listaEncabezados=["FECHA","TAREA"] 
            listadatos=[]	
            filas=len(tareas.index)	
            contador=2
            self.ui.tableWidget.setRowCount(filas)	
            self.ui.tableWidget.setColumnCount(contador) 
                
            for registros in tareas.values: 
                dato=(tuple(registros)) 
                listadatos.append(dato) 
        
                    
            fila=0
            for registro in listadatos: 
                columna=0 
                for elemento in registro: 
                    celda=QTableWidgetItem(str(elemento)) 
                    self.ui.tableWidget.setItem(fila,columna,celda) 			
                    columna=columna+1 
                fila=fila+1																	
            self.ui.tableWidget.setHorizontalHeaderLabels(listaEncabezados)
            self.ui.tableWidget.setSortingEnabled(True)

            
            self.ui.tableWidget.setColumnWidth(0,200)
            self.ui.tableWidget.setColumnWidth(1,443)

        except:
            self.ui.titulo.setText("No Hay Tareas Registradas")

    def atras(self):
        self.parent().show()
        self.close()



class VentanaRecordar(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaRecordar,self).__init__(parent)
        self.ui=Ui_Ventana_Recordatorio()
        self.ui.setupUi(self)
        self.ui.mensaje.setText("POR FAVOR NO CIERRE ESTA VENTANA PARA PODER RECORDARLE SU TAREA")

        self.ui.regresar.clicked.connect(self.atras)

        self.ui.hacer.clicked.connect(self.hacer)


    def hacer(self):
        global recordatorio
        segundos=int(self.ui.min.value())
        minutos=segundos*60

        veces=int(self.ui.veces.value())
        if veces>0 and segundos>0:
            final=minutos
            self.ui.mensaje.setText("CONTANDO")

            for x in range(veces):
                time.sleep(final)
                notification.notify(
                title="NOTIFICACION",
                message = "¿Ya Hiciste tu tarea? :( ",
                timeout=15,
                )
                recordatorio+=1

            if recordatorio==veces:
                self.parent().show()
                self.close()
        else:
            pass

        
        

    def atras(self):
        self.parent().show()
        self.close()


class VentanaEliminar(QMainWindow):
    def __init__(self,parent=None):
        super(VentanaEliminar,self).__init__(parent)
        self.ui=Ui_Ventana_Eliminar()
        self.ui.setupUi(self)

        self.ui.regresar.clicked.connect(self.atras)
        self.ui.eliminar.clicked.connect(self.eliminar)

        try:
            tareas=pd.read_csv("Procesador de Tareas/archivos/Tareas.csv")
            listaEncabezados=["FECHA","TAREA"] 
            listadatos=[]	
            filas=len(tareas.index)	
            contador=2
            self.ui.tableWidget.setRowCount(filas)	
            self.ui.tableWidget.setColumnCount(contador) 
                
            for registros in tareas.values: 
                dato=(tuple(registros)) 
                listadatos.append(dato) 
        
                    
            fila=0
            for registro in listadatos: 
                columna=0 
                for elemento in registro: 
                    celda=QTableWidgetItem(str(elemento)) 
                    self.ui.tableWidget.setItem(fila,columna,celda) 			
                    columna=columna+1 
                fila=fila+1																	
            self.ui.tableWidget.setHorizontalHeaderLabels(listaEncabezados)
          

            
            self.ui.tableWidget.setColumnWidth(0,100)
            self.ui.tableWidget.setColumnWidth(1,220)

          
            for x in range(1,filas+1):
                self.ui.opciones.addItem(str(x))

        except:
            self.ui.titulo.setText("No Hay Tareas Registradas")

    def eliminar(self):
        try:
            tareas=pd.read_csv("Procesador de Tareas/archivos/Tareas.csv")
            seleccion=int(self.ui.opciones.itemText(self.ui.opciones.currentIndex()))
            seleccion=seleccion-1
            tareas.drop([seleccion],axis="index",inplace=True)
            remove("Procesador de Tareas/archivos/Tareas.csv")

            ruta="Procesador de Tareas/archivos/Tareas.csv"

            tareas.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))

            tareas=pd.read_csv("Procesador de Tareas/archivos/Tareas.csv")
            listaEncabezados=["FECHA","TAREA"] 
            listadatos=[]	
            filas=len(tareas.index)	
            contador=2
            self.ui.tableWidget.setRowCount(filas)	
            self.ui.tableWidget.setColumnCount(contador) 
                
            for registros in tareas.values: 
                dato=(tuple(registros)) 
                listadatos.append(dato) 
        
                    
            fila=0
            for registro in listadatos: 
                columna=0 
                for elemento in registro: 
                    celda=QTableWidgetItem(str(elemento)) 
                    self.ui.tableWidget.setItem(fila,columna,celda) 			
                    columna=columna+1 
                fila=fila+1																	
            self.ui.tableWidget.setHorizontalHeaderLabels(listaEncabezados)
           

            
            self.ui.tableWidget.setColumnWidth(0,100)
            self.ui.tableWidget.setColumnWidth(1,220)

            self.ui.opciones.clear()
            for x in range(1,filas+1):
                self.ui.opciones.addItem(str(x))

            
        except:
            self.ui.titulo.setText("No Hay Tareas Registradas")






    def atras(self):
        self.parent().show()
        self.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    dialogo=VentanaP1()
    dialogo.show()
    sys.exit(app.exec_())